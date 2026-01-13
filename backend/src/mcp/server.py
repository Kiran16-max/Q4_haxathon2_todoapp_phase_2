# backend/src/mcp/server.py
from sqlmodel import Session
from uuid import UUID
from typing import Dict, Any, Callable
from src.mcp.tools.add_task import add_task_tool
from src.mcp.tools.list_tasks import list_tasks_tool
from src.mcp.tools.complete_task import complete_task_tool
from src.mcp.tools.delete_task import delete_task_tool
from src.mcp.tools.update_task import update_task_tool

class MCPServer:
    """
    Model Context Protocol (MCP) server that connects AI models with backend tools.
    """
    
    def __init__(self, session: Session, user_id: UUID):
        self.session = session
        self.user_id = user_id
        self.tools: Dict[str, Callable] = {
            "add_task": lambda params: add_task_tool(params, self.session, self.user_id),
            "list_tasks": lambda params: list_tasks_tool(params, self.session, self.user_id),
            "complete_task": lambda params: complete_task_tool(params, self.session, self.user_id),
            "delete_task": lambda params: delete_task_tool(params, self.session, self.user_id),
            "update_task": lambda params: update_task_tool(params, self.session, self.user_id),
        }
    
    def call_tool(self, tool_name: str, params: Dict[str, Any]) -> Any:
        """
        Call a specific tool with the given parameters.
        
        Args:
            tool_name: Name of the tool to call
            params: Parameters to pass to the tool
            
        Returns:
            Result from the tool execution
        """
        if tool_name not in self.tools:
            raise ValueError(f"Unknown tool: {tool_name}")
        
        tool_func = self.tools[tool_name]
        return tool_func(params)
    
    def get_available_tools(self) -> list:
        """
        Get a list of available tools.
        
        Returns:
            List of available tool names
        """
        return list(self.tools.keys())