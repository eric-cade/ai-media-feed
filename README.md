# Fathom
### *An experimental platform for AI-mediated information systems*

Fathom is an open-source prototype designed to explore how **AI-generated content behaves under feedback loops, engagement dynamics, and recursive generation**.

Rather than optimizing for growth or virality, Fathom is intentionally structured as a **model system**: a small, inspectable environment for studying how ranking, novelty, and user interaction shape the evolution of AI-generated media over time.

This project sits at the intersection of **applied AI, multi-agent dynamics, and human–machine interaction**, with an emphasis on system behavior, failure modes, and responsible integration.

---

## What Fathom Explores

Fathom is built to investigate questions such as:

- How does recursive AI generation affect content diversity over time?
- When do engagement-based feedback loops amplify novelty vs. collapse into homogenization?
- How does visibility bias shape which ideas survive and propagate?
- What failure modes emerge when AI systems are embedded in attention-driven environments?

The goal is not to answer these definitively, but to provide a **concrete, runnable system** where such dynamics can be observed, modified, and tested.

---

## Core System Concepts

- **AI-generated posts** created on demand  
- **Topic-based spaces** functioning as lightweight information ecosystems  
- An **endless vertical feed** ranked by engagement and novelty signals  
- **Recursive content evolution**, where posts can spawn derivative content via user interaction (“Power”)  
- **Emergent behavior** driven by ranking logic, user input, and generative feedback  

Fathom is intended as a **research and experimentation platform**, not a production social network.

---

## What’s Included in This Repository

This open-source release provides everything needed to **run, inspect, and extend the system locally**, without external API keys:

- **Godot client**
  - UI
  - Feed logic
  - Ranking & visibility behavior
  - Interaction handling
- **Local dummy backend**
  - Mock AI-generated posts
  - Placeholder endpoints matching the real API structure
  - Safe offline experimentation environment
- **Backend API documentation**
  - Clear description of the real backend interface
  - Enables custom backend implementations or alternative AI integrations

### What’s *not* included

The full production backend used in the author’s deployed instance is **not open-sourced**.  
It includes live data storage, real AI model calls, and production ranking logic.

This separation is intentional: the repository focuses on **system structure and behavior**, not operational infrastructure.

---

## System Architecture Overview

Fathom is deliberately modular so that **generation, ranking, and backend behavior can be modified independently** for experimentation.

### 1. Godot Client (included)

Responsible for:
- Rendering the feed and UI
- Displaying posts and interactions
- Triggering recursive generation events (“Power”)
- Requesting new content
- Applying ranking and visibility logic on the client side

### 2. Dummy Backend (included)

Provides:
- Placeholder generated content
- Mock API endpoints matching the real backend
- A deterministic, offline testing environment

### 3. Real Backend (not included)

In the deployed version, the private backend:
- Stores real posts and engagement data
- Calls AI models to generate new content
- Implements the full ranking and evolution logic

The API shape is documented so others can implement their own backend if desired.

---

## Design Philosophy

Fathom is guided by a few core principles:

- **Minimal but expressive** — small systems that surface meaningful dynamics  
- **Inspectable** — behavior should be understandable, not opaque  
- **Experimental** — optimized for modification and learning, not polish  
- **Responsible** — focused on evaluation and failure modes, not hype  

This makes Fathom suitable for:
- Applied AI experimentation  
- Governance-adjacent research  
- Systems thinking and simulation  
- Educational exploration of AI feedback loops  

---

## Failure Modes & Limitations

Fathom intentionally exposes — rather than hides — system weaknesses, including:

- Feedback loops that can reduce diversity  
- Sensitivity to ranking parameter changes  
- Emergent dominance of certain content patterns  
- Tradeoffs between novelty, engagement, and stability  

These behaviors are **features of the experiment**, not bugs to be eliminated.

---

## Roadmap

Planned directions emphasize **evaluation and controlled experimentation**, not feature completeness:

- Post lineage visualization (“spawned from” indicators)
- Agent-driven feed dynamics
- Local LLM support
- Alternative ranking and visibility algorithms
- Plugin system for custom generators and evaluators
- Mobile-friendly layout
- Simulation instrumentation and metrics

See `roadmap.md` for more details.

---

## Running the Project

1. Clone the repository  
2. Open the `godot/` directory in **Godot 4.x**  
3. Run the project  
4. Posts will be generated using the local dummy backend  

To integrate a real AI backend, see:

`backend/api_structure.md`

## Contributing
Contributions are welcome, particularly in areas related to:

-Ranking and visibility experiments
-Evaluation tooling and metrics
-UI clarity and inspection tools
-Local AI integration
-Documentation and research use cases
If you’re new to open source, feel free to open an issue or start a discussion.

---

## License
MIT License — free for personal or commercial use.

---

## Contact/Context
This project is developed as part of a broader exploration of AI systems, simulations, and human–machine interaction.
It is intended to support public-interest technology, research-adjacent work, and responsible AI experimentation.
