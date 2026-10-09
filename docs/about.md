# About

Staff Engineer at Mozilla.ai, with extensive experience in distributed systems, authentication, platform engineering, and enterprise architecture.

## Background

My career has focused on building infrastructure and tooling that enables engineering teams to ship software faster and more reliably, with particular emphasis on authentication patterns, API design, microservices architecture, and platform engineering.

### Current

**Mozilla.ai** - Staff Engineer (2024-Present)
Building open infrastructure for AI agents.

- **[cq](https://github.com/mozilla-ai/cq)**: an open standard for shared agent learning. Agents store and query what other agents have already learned, so they stop rediscovering the same failures on their own. Think "Stack Overflow, but for agents". I started it and lead it. It plugs into Claude Code, GitHub Copilot, Cursor and other agent hosts, and [cq exchange](https://cq.exchange) (launched May 2026) is Mozilla.ai's hosted service built on top of it. I've talked about it at AI Native DevCon London and on GitHub's Open Source Friday.
- **apron**: small libraries for the plumbing every product ends up needing. [apron-auth](https://github.com/mozilla-ai/apron-auth) handles the OAuth protocol side (PKCE, code exchange, token refresh and revocation), and [apron-tools](https://github.com/mozilla-ai/apron-tools) wraps provider APIs with typed schemas, OAuth scope mappings and LLM function-calling definitions.
- **[mcpd](https://github.com/mozilla-ai/mcpd)**: a tool to declare and run MCP servers the same way from a laptop to production, with SDKs in Python, .NET, Go and Rust. It's also where my [thoughts on MCP identity](posts/mcp-identity-crisis.md) came from.

### Previous Experience

**HashiCorp** (2021-2024)
Vault Engineering team, working on enterprise secrets management for tier-0 financial institutions. Led initiatives around audit system enhancements, filtering and redaction capabilities, and data-driven quality improvements.

**NatWest Group** (2015-2021)
Principal Engineer role focusing on platform engineering and developer experience. Led enterprise tooling initiatives enabling self-service automation across the bank, reducing time-to-production while maintaining governance. Designed and delivered REST-based microservices, event-driven architectures, and integration with cloud platforms (AWS, PCF, HashiCorp Vault).

**Sage** (2019)
Technical Architect for Sage People Payroll. End-to-end ownership of technical solution design, including serverless AWS architecture (Lambda, SQS, DynamoDB, Fargate) integrated with Salesforce.

Earlier roles include Thomson Reuters, and various consulting positions focused on infrastructure, messaging systems, and enterprise application development.

This blog explores the gap between theoretical elegance and operational reality in production systems.

## Connect

- :fontawesome-brands-github: [github.com/peteski22](https://github.com/peteski22)
- :fontawesome-brands-linkedin: [linkedin.com/in/peter-d-wilson](https://linkedin.com/in/peter-d-wilson)
- :fontawesome-brands-bluesky: [@peteski22.bsky.social](https://bsky.app/profile/peteski22.bsky.social)
- :fontawesome-brands-mastodon: [@peteski22@mastodon.social](https://mastodon.social/@peteski22)
