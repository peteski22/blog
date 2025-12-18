---
date: 2025-12-18
authors:
  - peteski
categories:
  - AI
  - Architecture
  - Privacy
---

# Why I'm Building Toward Sovereign AI

I've been spending evenings and weekends on something that might sound idealistic: infrastructure for personal data sovereignty. But I'm not building it because I think it'll definitely work. I'm building it because the alternative - doing nothing - seems worse.

<!-- more -->

## The Problem

The AI industry runs on a surveillance economy. Your context - browsing history, messages, photos, location patterns, the texture of your daily life - gets harvested, aggregated, and used to train models. You're an unpaid data labourer for systems that may eventually replace you.

This isn't a conspiracy theory. It's the business model. "Free" services aren't free; you pay with your data, and that data has real value. Some economists call this technofeudalism - platforms extracting rent from users who can't meaningfully opt out. They use your context to build AI that serves their interests, not yours. And their interests are straightforward: returns for shareholders, leverage for owners.

## The Concept: Personal Context Infrastructure

I've been working to advance Personal Context Infrastructure (PCI), a concept introduced by Jad Esber and Apurva Chitnis at [koodos](https://blog.koodos.com/p/personal-context-infrastructure). The idea: a local-first architecture where your data stays on your devices.

The core ideas:

**Local-first storage.** Your data lives encrypted on devices you control, synced via CRDTs (using Yjs). No cloud service holds the plaintext.

**Local AI processing.** Small language models (Phi-3, Llama, Mistral) run on-device. Your AI assistant can actually know you - your notes, your preferences, your history - without any of that leaking to external services.

**Zero-knowledge verification.** When services need to verify something about you (age, credentials, income threshold), ZKPs provide the answer without revealing underlying data. You can't train on what you never received. Midnight's privacy-preserving blockchain handles this layer.

**Cryptographic policy enforcement.** User preferences are expressed in S-PAL (Sovereign Privacy & Access Language) - machine-readable policies that smart contracts on Cardano enforce. If your policy says "no access," the transaction fails mathematically. Yes, it's crypto - but proof-of-stake uses less energy than the AI training runs it's designed to constrain, and this is the utility critics always say blockchain should have.

**Community infrastructure.** Between "run your own server" (too hard) and "trust Big Tech" (defeats the purpose) lies a middle path: community organisations - libraries, co-ops, local tech groups - running sovereignty infrastructure for their members.

## Why This Matters for AI

The current trajectory has AI companies hoovering up everything to train ever-larger models. But there's another path: AI that comes to your data instead of your data going to their models.

Small models are getting remarkably capable. An iPhone can run a 3B parameter model locally. WebAssembly brings inference to browsers. The "you need massive scale" argument is weakening.

Sovereign AI means your personal assistant actually works for you. It has context about your life because it runs locally against your encrypted data - not because some company harvested that context and might use it against your interests.

## What I'm Building

I've been documenting the architecture and building initial implementations:

- Encrypted context storage using battle-tested CRDTs
- Identity management with ephemeral DIDs to prevent tracking
- Zero-knowledge proof services for verification without disclosure
- Smart contracts for policy enforcement
- Agent coordination layer
- Infrastructure tooling and specifications

It's early. The repos aren't public yet. But the design documents are taking shape, and the pieces are starting to connect.

## Why Bother?

I'm not certain this will succeed. But I'm certain that if we all shrug and accept surveillance as inevitable, it becomes inevitable. The technology for a different path exists. Someone has to build it.

If you're interested in data sovereignty, local-first architecture, or AI that actually serves users - I'll be sharing more as this develops.
