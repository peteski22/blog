---
date: 2026-02-04
authors:
  - peteski
categories:
  - AI
  - Infrastructure
  - Policy
---

# AI Growth Zones: Gift Horse or Trojan Horse?

In September 2025, the UK government [announced](https://www.gov.uk/government/news/ai-to-power-national-renewal-as-government-announces-billions-of-additional-investment-and-new-plans-to-boost-uk-businesses-jobs-and-innovation) an AI Growth Zone for the North East of England. The [headline numbers](https://www.northeast-ca.gov.uk/news/finance-and-investment/north-east-england-set-for-billions-in-investment-and-thousands-of-jobs-through-new-ai-growth-zone) sound impressive: £30 billion in potential investment, "up to 5,000 jobs", partnerships with Blackstone, OpenAI, and NVIDIA. Similar investments are happening globally. Microsoft alone is [spending $80 billion](https://www.cnbc.com/2025/12/19/data-center-deals-hit-record-amid-ai-funding-concerns-grip-investors.html) on AI datacentres this year.

This is genuinely exciting. Regions like the North East that have been economically neglected for decades deserve investment in future industries. I'm not arguing against it.

But I have concerns about what we're building, who will own it, and what happens to our data from day one.

<!-- more -->

## We've Been Here Before

I keep thinking about this pattern because we've seen it with other infrastructure. Water, gas, electricity, rail, broadband. All pitched as bringing investment and efficiency. And in the short term, they may have. But over time, the ownership structure matters enormously.

Take water. The UK privatised water companies in 1989. Nearly four decades later, Thames Water is on the brink of collapse, pipes leak billions of litres, and sewage is pumped into rivers because the infrastructure wasn't maintained. Where did the money go? Billions extracted in dividends to shareholders. CEO bonuses paid whilst treatment plants crumbled. And now customers are being asked to fund repairs through price rises, paying twice for infrastructure that should have been maintained all along.

The worst part? You can't switch. You can't choose a different provider. You can't run a competing pipe into your home. It's a natural monopoly, and once private interests own it, you're captive. The only leverage left is regulation, and we've seen how well that works when the regulator is underfunded, the companies have armies of lawyers, and the revolving door between regulator and regulated keeps spinning.

AI infrastructure feels similar. The narrative is compelling: "AI will transform our region." The construction phase will deliver real activity: jobs, spending, ribbon-cuttings. But datacentres don't employ many people once they're operational. The [first phase approval](https://www.bbc.co.uk/news/articles/clyd1enx3p4o) for the Blyth site revealed the actual numbers: "about" 400 permanent staff once fully operational, with claims of "up to 2,700" indirect jobs. That's a long way from the "5,000 jobs" headline. For context, Microsoft's 800,000 sq ft Columbia Data Center in Quincy, Washington [employs about 50 people](https://en.wikipedia.org/wiki/Columbia_Data_Center).

## The Extraction Concern

Here's what worries me most: infrastructure ownership can be renegotiated over time, but data extracted is gone forever.

The North East zone will host [Stargate UK](https://www.northeast-ca.gov.uk/news/finance-and-investment/north-east-england-set-for-billions-in-investment-and-thousands-of-jobs-through-new-ai-growth-zone), a partnership between Nscale, OpenAI, and NVIDIA. OpenAI is taking up to 8,000 GPUs initially, potentially expanding to 31,000. That's serious compute. And compute needs data.

Look at where these companies are headquartered. OpenAI: San Francisco. NVIDIA: Santa Clara, California. QTS, who are building the Blyth datacentre: Kansas City, Missouri. The profits, the high-value jobs, the strategic decisions, they flow back to the US. Nscale is UK-headquartered, which is something, but they're backed by Norwegian and international capital.

And let's not pretend these companies have a great track record on paying tax where they operate. We've watched Google and Amazon structure their UK operations to minimise their contributions for years. Why would this be different?

The pitch to local businesses will sound reasonable: "AI will make you more productive." Maybe it will, for some businesses. But which ones? Will Jim's Butcher shop become more productive? Will the local corner shop? Or is this really about streamlining services, which often means cutting jobs? The stats celebrating "5,000 new jobs created" rarely mention how many were lost because the C-suite wanted AI everywhere to justify their bonuses.

The implicit trade for any business that does adopt these services: your business data, your customer interactions, your operational patterns. All feeding models that will be sold back to you as services, priced however the provider chooses. Unlike a road or a power plant, you can't nationalise a dataset that's already been absorbed into a foundation model. Once the data is extracted, it's extracted.

## What Would Responsible Investment Look Like?

I'm not anti-investment. I'm not even anti-hyperscaler. Private capital takes risks that public bodies often can't or won't. But I think there are structures that would genuinely benefit regions rather than just extracting from them.

**Progressive community ownership.** Rather than outright private ownership, structure investments with buyback provisions. The private company takes the initial risk and makes their agreed return, but over time ownership progressively transfers to a community trust or municipal entity. Not a vague promise for decades hence, but 10-15 years with clear milestones. This isn't radical. It's how some infrastructure projects already work. The difference is making it the expectation, not the exception.

**Co-operative and distributed models.** Not everything needs to be hyperscale. Smaller, distributed datacentres could be owned and operated by co-operatives or municipal bodies. [Guifi.net](https://guifi.net/) in Catalonia runs over 37,000 community-owned network nodes, proving that community infrastructure can work at scale. [El Servidor del Barri](https://barri.elmercatcultural.cat/) in Barcelona's Collserola neighbourhoods runs community cloud services (password management, file storage, even a local AI experiment) all owned and operated by residents. [Stockholm](https://www.stockholmexergi.se/en/heat-recovery/) already uses datacentre waste heat to warm 10,000 apartments through its district heating network, turning a cost into a community benefit.

**Data sovereignty from day one.** Whatever the ownership model for physical infrastructure, data sovereignty needs to be baked in from the start. Local businesses should be able to use AI services without surrendering their data permanently. Citizens should have cryptographic control over their personal data. The default should be "data stays local" with explicit, auditable exceptions.

This is the problem I'm working on with [Personal Context Infrastructure](https://peteski22.github.io/pci-docs/): technical architectures that make data sovereignty enforceable, not just promised.

## The "AI Skills" Question

There's a secondary pattern worth watching. The government recently [announced](https://www.gov.uk/government/news/free-ai-training-for-all-as-government-and-industry-programme-expands-to-provide-10-million-workers-with-key-ai-skills-by-2030) a programme to provide "10 million workers with key AI skills by 2030". Sounds impressive.

Look closer. Browse the [AI Skills Hub](https://aiskillshub.org.uk/aiskillsboost/) and count the Microsoft courses: "Get Started with Agents", "Get started with Microsoft 365 Copilot", "Craft effective prompts for Microsoft 365 Copilot", "Copilot video tutorials". The training takes "as little as under 20 minutes". The skills taught: "use of AI for tasks like drafting text, creating content and completing administrative tasks".

The founding partners delivering this: Accenture, Amazon, Barclays, BT, Google, IBM, Intuit, Microsoft, Sage, Salesforce, SAS. Want something more substantive? The Oxford, DataCamp, and Udemy courses are listed as "Fee Payable". The free stuff is the vendor onboarding material.

This isn't skills development. It's teaching people to prompt a chatbot, delivered by the companies who sell the chatbots. The "skill" transferred is how to become a customer.

Think about where the money flows. Businesses adopt Microsoft 365 Copilot at £30/user/month. That flows to Microsoft's shareholders, funds engineering salaries in Seattle and San Francisco, and builds capabilities in the US tech ecosystem. The UK worker becomes a consumer of AI, not a builder of it. The high-value jobs, the ML engineers, the infrastructure architects, the product managers, they stay in Silicon Valley. We get a 20-minute course on how to prompt.

This is a government initiative. It should be about lifting UK citizens, building UK capabilities, creating UK jobs and UK innovation. We're a services economy looking for the next thing. AI could be that, but not if we just become a market for US products. Not if we subsidise the further concentration of AI expertise in a handful of American companies.

Genuine skills investment would look different: training people to run local models, understand AI architectures, build rather than just consume. The North East announcement mentions partnerships with Newcastle, Durham, Sunderland, and Northumbria universities for training programmes. I hope those programmes create genuine local capability, not just another channel for cloud AI adoption.

## AI Infrastructure as Utility

I increasingly think AI infrastructure should be treated like other utilities: water, electricity, transport. Something too important to leave entirely to market dynamics and shareholder returns.

And here's the concern: AI infrastructure has natural monopoly characteristics. Once a hyperscaler owns the datacentres, the power contracts, the cooling infrastructure, and the talent pipeline in a region, competition becomes very difficult. You can't easily run a competing set of cables and cooling systems. The switching costs become enormous. And by then, they also have your data.

That doesn't necessarily mean public ownership of everything. Shared ownership models could work, where a percentage is privately held but the community stake grows over time as the initial investment is repaid. Co-operative models could work for smaller-scale infrastructure. Municipal ownership could work for community datacentres.

What concerns me is accepting the default assumption that private ownership with no community endpoint is the only option. We tried that with water. We're watching the consequences flow into our rivers.

## The Real Question

The North East deserves this investment. Post-industrial regions across the UK deserve investment in future industries. I genuinely hope the AI Growth Zones create sustainable economic development.

But let's be honest about what's being offered. In 10 years, will the community own meaningful infrastructure? Will local businesses retain sovereignty over their data? Will we have built genuine UK AI capability, or just become a better customer for American tech giants?

The extraction doesn't start in 20 years. It starts the moment the first byte of data leaves a local business for a US-hosted model. It starts when the profits flow to shareholders in Kansas City and Santa Clara. It starts when our "AI skills programme" teaches people to be consumers rather than creators.

The Trojans thought they'd won a war. They wheeled the gift inside the gates themselves.

---

*I'm a Staff Engineer at [Mozilla.ai](https://mozilla.ai/) working on trustworthy AI infrastructure, currently studying AI ethics and regulation at Oxford. [Personal Context Infrastructure](https://peteski22.github.io/pci-docs/) is my attempt to build the data sovereignty layer I think we'll need.*
