"""
SwarmCoordinator: The raid leader of our agent swarm fr fr
"""
import os
import json
import sqlite3
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime

import typer
from rich import print
from github import Github
from github.Issue import Issue
from github.WorkflowRun import WorkflowRun

class SwarmCoordinator:
    def __init__(self) -> None:
        self.gh = Github(os.getenv("GITHUB_TOKEN"))
        self.memory_path = Path(".memory/swarm.db")
        self.setup_memory()
        
    def setup_memory(self) -> None:
        """Set up that persistent memory storage no cap"""
        self.memory_path.parent.mkdir(exist_ok=True)
        self.conn = sqlite3.connect(self.memory_path)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                agent_id TEXT,
                timestamp TEXT,
                context TEXT,
                memory_content TEXT
            )
        """)
        self.conn.commit()
    
    def store_memory(self, agent_id: str, context: str, content: Dict[str, Any]) -> None:
        """Remember stuff like an elephant with a photographic memory"""
        self.conn.execute(
            "INSERT INTO memories VALUES (?, ?, ?, ?)",
            (agent_id, datetime.utcnow().isoformat(), context, json.dumps(content))
        )
        self.conn.commit()
    
    def recall_memories(self, agent_id: str, context: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Pull up those memories faster than a speedrunner's muscle memory"""
        memories = self.conn.execute(
            "SELECT memory_content FROM memories WHERE agent_id = ? AND context LIKE ? ORDER BY timestamp DESC LIMIT ?",
            (agent_id, f"%{context}%", limit)
        ).fetchall()
        return [json.loads(m[0]) for m in memories]
    
    def handle_issue(self, issue_data: Dict[str, Any]) -> None:
        """Someone opened a support ticket in our Discord"""
        print(f"[bold cyan]New task received: {issue_data['title']}")
        
        # Store task in memory
        self.store_memory(
            "coordinator", 
            "task_assignment",
            {"task_id": issue_data["number"], "title": issue_data["title"]}
        )
        
        # Analyze task and delegate to appropriate agent
        # This be where the magic happens fr fr
        
    def handle_workflow_completion(self, workflow_data: Dict[str, Any]) -> None:
        """One of our agents finished their quest"""
        print(f"[bold green]Workflow completed: {workflow_data['workflow']}")
        
        # Update task status and coordinate next steps
        # More magic here no cap
        
def main(
    event_type: str = typer.Option(..., "--event-type"),
    event_data: str = typer.Option(..., "--event-data")
) -> None:
    """Main entry point for our coordinator agent"""
    coordinator = SwarmCoordinator()
    data = json.loads(event_data)
    
    if event_type == "issues":
        coordinator.handle_issue(data)
    elif event_type == "workflow_run":
        coordinator.handle_workflow_completion(data)
    
if __name__ == "__main__":
    typer.run(main)