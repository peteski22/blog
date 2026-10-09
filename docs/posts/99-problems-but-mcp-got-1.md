---
date: 2026-11-17
authors:
  - peteski
categories:
  - AI
  - Architecture
  - Identity
  - MCP
---

# I got 99 problems, but MCP got 1

Almost a year ago, while working on an open source project at Mozilla AI named [mcpd](https://blog.mozilla.ai/meet-mcpd-requirements-txt-for-agentic-systems/) (also a [plugin system](https://blog.mozilla.ai/mcpd-plugins-extend-your-agent-infrastructure-without-touching-your-code/) and [proxy](https://blog.mozilla.ai/mcpd-proxy-centralized-tool-access-for-ai-agents-in-vs-code-cursor-and-beyond/)), I became frustrated in my dealings with the Model Context Protocol (MCP). So, like a good keyboard warrior, I [wrote about it on the internet](mcp-identity-crisis.md).

Since that time, a lot has changed in the fast-moving world of AI and with MCP. A few times over these months I thought: I should do a follow-up post, but then work got in the way. But fear not... the time has come.

<!-- more -->

I'll start by briefly explaining why I was making a racket in the first place. Yes it was partially therapeutic, but I wanted to draw attention to a problem I saw in MCP, which was that there was no standard way to get a user's identity to systems 'upstream' of an MCP server. My proposal to stoke debate was an [upstream_identity](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/1827) field (it closed on 2026-09-25 when Discussions became meeting-notes only), looking back at this now it probably wasn't the right solution, but the important thing was that the problem existed (and still does to some extent), and I really felt like it should be talked about.

Better to get this out of the way early, and my apologies...

My post got a few things wrong:

* I said "No action taken" on [MCP#195](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/195), but it was closed as completed, and the 2025-06-18 spec made `WWW-Authenticate` a MUST.
* [MCP#234](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/234#discussioncomment-13054006) was closed by its own author in May 2025, months *before* URL mode existed, not after it as I said.

The proposal also got a few things wrong:

* The GitHub, Grafana and Stripe MCP servers I cited in my examples were `stdio` servers, and so were following the spec in using environment variables
* I suggested sending a non-MCP token to the server: forbidden in the spec
* The "no passthrough" rule does have wide support outside MCP (for example, the [IETF WIMSE AIMS draft](https://datatracker.ietf.org/doc/draft-ietf-wimse-aims/))
* Probably myriad other things

But, I say again (maybe for my pride, or ego) the real issue was that nothing said where the upstream token comes from.

OK, so what changed in the months between rant and return-rant? MCP got a long list...

URL mode elicitation, Enterprise-Managed Authorization (EMA), stateless protocol, header-based routing and `iss` validation... and Dynamic Client Registration (DCR) was deprecated and replaced with Client ID Metadata Documents (CIMD).

The vendors I used as examples also moved towards using OAuth for their hosted servers (looking at you GitHub, Stripe, Grafana Cloud), but still use tokens for the local servers.

They also seem to have agreed that there are still gaps to fill, from the [roadmap](https://modelcontextprotocol.io/development/roadmap):

> "MCP authorization assumes a person with a browser at consent time... Existing MCP servers lean on pasted API keys and long-lived refresh tokens."

So where do things stand when it comes to my desire to have this upstream situation sorted?

* User with a browser: Covered via OAuth and [EMA](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization).
* Agent acting as itself (CI, workload): Draft [Client Credentials](https://modelcontextprotocol.io/extensions/auth/oauth-client-credentials) and [Workload Identity Federation SEP-1933](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1933).
* Agent acting on behalf of a user who is not present: Partly covered by [ID-JAG](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/) with a refresh token after one login. There is no standard way to name the agent, no standard for a 2nd hop (upstream).

Since the 2nd hop is a choice, and the Auth group has discussed changes that only affect 'server internals' as things that 'may not require MCP standardization at all' ([Auth group notes, Feb 2026](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/2234)), what we see happening is that gateways (e.g. agentgateway, Cloudflare, ContextForge, Kong, Teleport etc.) fill the gap with their own formats, the result of which is that the identity travels upstream... differently in every product.

And these gateways aren't going anywhere. Enterprises want one central place for audit, tool and MCP server RBAC, keeping secrets off developer machines, and of course a kill switch when needed. But central audit is only as good as the identity behind it. The gateway's log might say "Peter, using agent qwerty123, called create_issue on the GitHub server", but if the gateway then calls GitHub with one shared token, GitHub's own log just says "gateway_bot". GitHub's per-user permissions don't apply, GitHub can't revoke just me, and if that one token leaks, it works for everyone.

ID-JAG seems like the new heir apparent, since seemingly moving from concept to production this year (2026), folks that have been interacting with the MCP ecosystem will have likely seen or heard of the 'Identity Assertion JWT Authorization Grant' (rolls right off the tongue doesn't it?); it's what MCP's EMA extension is built on top of.

**TL;DR**: Similar to when you land in another country and your phone just works without having to sign up to a local network. The foreign network asks your home network "is this one of yours, and are they allowed to roam?", and when it gets told 'yes' it lets you use it. The network back home controls your access, and can restrict you from anywhere. That's ID-JAG for applications, letting one application access another application's resources on your behalf without signing in again or approving every connection by hand.

ID-JAG is supported in Okta and PingFederate, with others such as Keycloak, Auth0 and WorkOS starting to accept it (experimental or early access). So adoption is growing, although Microsoft Entra notably doesn't issue it, and goes its own way with on-behalf-of and Agent ID.

But ID-JAG on its own doesn't close the gap:

* It can't be reused for the next system. The draft says a new one "MAY be issued", but not how a server in the middle should ask for one.
* The "who is acting" (`act`) field is optional, so the agent can drop out of the picture.
* Every app has to be set up to trust your IdP first.

So, apart from that, is everything done, solved, hooray? Not quite yet... but we do trust our identity providers for all sorts of other things all the time:

* SSO: more or less every SaaS product will let your company IdP log people in.
* Cloud workload federation (AWS, GCP, Azure): Will take a signed token from an outside identity provider, e.g. GitHub Actions, and hand back short-lived API tokens (no static secrets!)

'Oh yeah?' you might say, and, the IETF even has a name for when you do this across organisations: [Identity and Authorization Chaining Across Domains](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-chaining/).

It's in the RFC Editor queue, so almost, almost there. And here's a bit I liked from a different draft, the [IETF WIMSE AI Identity Management System draft](https://datatracker.ietf.org/doc/draft-ietf-wimse-aims/) (section [10.8](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-aims-00#section-10.8)):

> "It is an anti-pattern for Tools to forward access tokens it received from the Agent to Services or Resources"

But in that same section it points at identity chaining as the way for a tool to get a token for the next system:

> "When the Tool needs access to a resource protected by an authorization server other than the Tool's own authorization server, the OAuth Identity and Authorization Chaining Across Domains ([OAUTH-ID-CHAIN]) can be used to obtain an access token from the authorization server protecting that resource."

So the "don't pass it through" rule **and** the "here's how you do the next hop" answer can live side by side. A handful of SaaS vendors (Slack, Linear, Atlassian and friends) already trust our IdPs via EMA, but only for their own MCP servers. What's missing is the rest of them doing the same, and for their APIs in general, so a gateway or server in the middle can make that next hop the same way cloud providers already let workloads do (not just logged-in humans).

I don't care **how** it happens, but what I hope to see happen is:

* MCP documents one standard way for a server (or gateway) to make that 2nd hop built on things that already exist (the token exchange, the identity chaining, ID-JAG).
* The tokens have a shared format that carries who the user is, and which agent is acting on behalf of that user; so every product doesn't have to invent its own claims.
* A 1st class/standard path where we have agents working on behalf of users in a browserless setting.
* A 'best practices' document for gateways (the Auth group said back in February that this area was "somewhat underdocumented", and gateways are where a lot of enterprises are landing).
* More SaaS vendors accept assertions from customer IdPs like the cloud providers already do.

The problem is on the MCP roadmap, progress is happening, this last step is about the same trust we already give to cloud APIs.

!!! note
    If by some chance anyone who's part of the Auth group reads this blog post, can I highlight that the [Auth IG charter](https://modelcontextprotocol.io/community/interest-groups/auth) says notes get cross-posted to GitHub Discussions. Please post the Auth group notes to GitHub again. The last ones there are from Feb 2026.
