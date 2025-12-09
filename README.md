# AI Media Feed (Open Source Prototype)

A generative, topic-based media feed built with Godot Engine.

This project explores a new kind of media ecosystem where:

- AI generates posts on demand
- Topics act like lightweight “subreddits”
- An endless vertical feed is ranked by engagement and novelty
- Users can “power” posts to spawn new, hybrid content

This open-source release includes:

- The **Godot client** (UI + feed logic)
- A **local dummy backend** (for development/testing without API keys)
- Documentation for the **backend API structure**

> The full production backend (used in my personal deployed version) is not included here.  
> Only the client, developer tools, and local backend simulator are open-sourced.

---

## Features

- **Infinite scrolling feed**
- **Topic/category selector**
- **Template-based post generation (dummy backend)**
- **Local backend simulator** — no API keys required
- **Modular architecture** for plugging in your own real backend
- Support for **post evolution** via the “Power” interaction

---

## How It Works (Architecture Overview)

### 1. Godot Client (in repo)
Responsible for:
- Rendering the feed
- Expanding posts and showing interactions
- Triggering "Power" events
- Requesting and displaying generated posts
- Ranking & visibility logic on the client side

### 2. Dummy Backend (in repo)
Provides:
- Placeholder generated posts
- Mock endpoints matching the real API structure
- A safe offline test environment

### 3. Real Backend (not included)
A private backend (deployed on Railway) that:
- Stores real posts & engagement
- Calls AI models (e.g., OpenAI) to generate new content
- Implements the true post ranking system

The repo documents the API shape so anyone can build their own backend if desired.

---

## Roadmap

Planned directions include:

- UI/UX improvements  
- **Post evolution & lineage system** (visible “spawned from” indicators)  
- Local LLM support  
- Agent-driven feed dynamics  
- Mobile-friendly layout  
- Plugin system for custom generators & ranking algorithms  

See `roadmap.md` for more details.

---

## Running the Project

1. Clone the repo  
2. Open the `godot/` directory in **Godot 4.x**  
3. Run the project  
4. Posts will be generated using the local dummy backend  
5. To integrate with a real AI backend, see `backend/api_structure.md`

---

## Contributing

Contributions are welcome — especially around:

- UI/UX  
- Local AI support  
- Ranking logic experiments  
- Mobile layout  
- Generation templates

If you're new to open source, feel free to open an issue or discussion.

---

## License

MIT License — free for personal or commercial use.
