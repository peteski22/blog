---
date: 2025-12-27
authors:
  - peteski
categories:
  - AI
  - Architecture
  - Privacy
  - Open Source
---

# Personal Context Infrastructure: The Repos Are Public

Last week I wrote about building toward sovereign AI - infrastructure that keeps your data local while letting AI actually help you. Today the repositories are public. Here's what's in them...

<!-- more -->

## The Architecture

PCI has five layers, each with its own repository:

**Layer 1: Context Store** ([pci-context-store](https://github.com/peteski22/pci-context-store))
Encrypted local storage using AES-256-GCM. Your data stays on your devices, synced via CRDTs when you have multiple. Vector embeddings via sqlite-vec enable semantic search over your personal context. Also caches ZKPs for reuse across services. Nothing leaves your device unless you want it to.

**Layer 2: Personal Agent** ([pci-agent](https://github.com/peteski22/pci-agent))
Runs small language models locally - Phi-3, Llama, Mistral, whatever fits your hardware. The agent queries your encrypted context store and enforces policies before responding. Your AI assistant actually runs on your machine.

**Layer 3: Smart Contracts** ([pci-contracts](https://github.com/peteski22/pci-contracts))
Cardano contracts that flip who sets the terms. You define the policy; requesters agree to it or don't get access. The opposite of clicking "I agree" on terms you didn't write. Commitments are recorded on-chain - doesn't prevent future misuse, but makes it provable.

**Layer 4: Zero-Knowledge Proofs** ([pci-zkp](https://github.com/peteski22/pci-zkp))
Midnight integration for verification without disclosure. Prove you're over 18 without revealing your birthdate. Prove you have a credential without exposing which one. Proofs are cached and reusable - verify once, use many times without paying repeatedly. Services get the answer they need; you keep the data they don't.

**Layer 5: Identity** ([pci-identity](https://github.com/peteski22/pci-identity))
DID management with ephemeral identities per interaction. No cross-service tracking. Each service sees a different you, unlinkable to your others. But you can prove linkage to your root identity when needed - for legal claims or if law enforcement requires it.

## Supporting Repositories

- [pci-spec](https://github.com/peteski22/pci-spec) - S-PAL schema definitions and protocol specifications
- [pci-docs](https://github.com/peteski22/pci-docs) - Architecture documentation and concept explanations
- [pci-infra](https://github.com/peteski22/pci-infra) - Docker Compose configurations for local development

## Current State

The project is in the very early stages. There are initial implementations for some pieces - encryption, vector storage, DID generation, contract structure - but plenty of GitHub issues waiting to be tackled. This is scaffolding, not a finished building.

What's in place:
- AES-256-GCM encryption with PBKDF2 key derivation
- SQLite persistence with sqlite-vec for vector search
- DID generation and management (did:key method)
- Cardano smart contract validators (currently using Aiken)
- TypeScript SDK for ZKP service integration

What's coming:
- Y.js CRDT sync across devices
- Local embedding model integration
- Full Midnight testnet deployment
- Community node infrastructure

## Why Open Source?

The whole point of data sovereignty is that you don't have to trust anyone. Open source means you can verify. You can run it yourself. You can modify it. If I disappear tomorrow, the code still exists.

Also: I can't build this alone. The intersection of local-first storage, small language models, zero-knowledge proofs, and smart contracts is genuinely hard. If this idea resonates with you, contributions are welcome.

## Get Involved

If any of this sounds interesting, have a poke around. The [pci-spec](https://github.com/peteski22/pci-spec) repo has the S-PAL specification if you want to understand the policy language, and [pci-docs](https://github.com/peteski22/pci-docs) explains how the layers fit together.

I'd genuinely like this to be a community effort rather than a solo project. If you're into encrypted storage, local AI, ZKPs, Cardano, or just the broader data sovereignty question - open an issue, submit a PR, or just say hello. If there's enough interest I'll turn on GitHub Discussions so we have somewhere to chat that isn't issue trackers.

Remember when you could buy something without handing over your life story? The corner shop model: you pay, you get the thing, transaction done. No loyalty card, no account, no "personalised experience" that's really just a profile being built on you. That's what we're trying to bring back - but for the AI era.
