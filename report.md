# Project 1 Report: Intelligent Search Visualizer

> [!IMPORTANT]
> **AUTOGRADER COMPLIANCE INSTRUCTIONS:**
> This report is parsed automatically by the autograder. To ensure you receive full credit for your work:
> 1. **Do not modify** the section headers (`## ...`) or bold field keys (e.g., `**Name:**`, `**Selected Region:**`, `**Live Deployment URL:**`, etc.).
> 2. **Write your answers directly after** the colon `:` of each field, replacing the placeholder text completely (including the outer brackets `[` and `]`).
> 3. **Maintain the file structure**. Changing headers, bold titles, or deleting lines can cause the autograder to miss your responses and award 0 marks.

---

## Student Information 
- **Name:** Abdoulaye Diallo
- **UID (netID):** adial9
- **UIN:** 654580279

---

## Section 1: Selected City Region
- **Selected Region:** Illinois USA

---

## Section 2: Map Graph Configuration
- **Total Cities Configured:** 22
- **Total Connection Edges:** 35
- **Graph Fully Connected:** Yes

---

## Section 3: Local Verification & Search Algorithms
*Check the algorithms you successfully ran and verified on your local development server by placing an `x` in the brackets (e.g., `[x]`):*
- [x] Breadth-First Search (BFS)
- [x] Depth-First Search (DFS)
- [x] Uniform Cost Search (UCS)
- [x] Iterative Deepening Search (IDS)
- [x] Greedy Best-First Search (Greedy)
- [x] A* Search (A*)

---

## Section 4: Deployed and Presentation Information
- **Deployment Platform:** Render
- **Live Deployment URL:** https://cs411-project01.onrender.com/
- **Video Presentation Link:** [Provide an accessible link to your 5–7 minute video presentation]

---

## Section 5: Discussion
- **Which search algorithm is best for this route finding problem?** 
    I think A* is a good choice for this route finding problem because it uses both the path cost and the estimated distance to the destination. In my test from Chicago, IL to Waukegan, IL, A* found the lowest cost path of 42.15 and expanded only 4 nodes.
- **Search Efficiency (Nodes expanded/time taken comparison):** For my Chicago, IL to Waukegan, IL test, BFS expanded 8 nodes and had a cost of 42.15. DFS expanded 14 nodes and had a cost of 423.84. UCS  expanded 12 nodes and had a cost of 42.15. IDS expanded 12 nodes and had a cost of 42.15. Greedy expanded 4 nodes and had a cost of 55.91. A* expanded 4 nodes and had a cost of 42.15. Greedy and A* expanded the fewest nodes, but A* found the lower-cost path. I did not measure the actual runtime, so I compared the algorithms using nodes expanded and path cost.

- **Link the idea of search algorithm to today Generative AI.** 
    Search algorithms are related to Generative AI because both can explore different possibilities to find a good result. Different search algorithms use different ways to decide which option to explore next. Generative AI can also explore different possible answers and choose a useful result.