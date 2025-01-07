"""
Memory module - Persistence cleaner than my git history fr fr 🧠
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional


@dataclass
class MemoryEntry:
    content: Any
    timestamp: datetime
    tags: List[str] = field(default_factory=list)
    importance: float = 1.0  # How critical this memory is fr fr


class MemoryStore(ABC):
    """Base class for memory storage (more reliable than my actual memory)"""

    @abstractmethod
    async def store(self, key: str, entry: MemoryEntry) -> None:
        """Save something for later (like my todo list but it actually works)"""
        pass

    @abstractmethod
    async def retrieve(self, key: str) -> Optional[MemoryEntry]:
        """Find that memory (faster than finding my keys)"""
        pass

    @abstractmethod
    async def forget(self, key: str) -> None:
        """Sometimes we need to let go (like my old code)"""
        pass


class InMemoryStore(MemoryStore):
    """Keeps memories in RAM (like Chrome with my tabs)"""

    def __init__(self) -> None:
        self._store: Dict[str, MemoryEntry] = {}

    async def store(self, key: str, entry: MemoryEntry) -> None:
        self._store[key] = entry

    async def retrieve(self, key: str) -> Optional[MemoryEntry]:
        return self._store.get(key)

    async def forget(self, key: str) -> None:
        if key in self._store:
            del self._store[key]


class PersistentStore(MemoryStore):
    """Keeps memories on disk (more permanent than my commitment issues)"""

    def __init__(self, path: str) -> None:
        self.path = path
        # TODO: Implement actual persistence
        self._store: Dict[str, MemoryEntry] = {}

    async def store(self, key: str, entry: MemoryEntry) -> None:
        # TODO: Actually write to disk
        self._store[key] = entry

    async def retrieve(self, key: str) -> Optional[MemoryEntry]:
        # TODO: Actually read from disk
        return self._store.get(key)

    async def forget(self, key: str) -> None:
        # TODO: Actually delete from disk
        if key in self._store:
            del self._store[key]


class MemoryManager:
    """Manages agent memories (more organized than my thoughts)"""

    def __init__(self, store: MemoryStore) -> None:
        self.store = store

    async def remember(
        self, key: str, content: Any, tags: Optional[List[str]] = None
    ) -> None:
        """Save a memory fr fr"""
        entry = MemoryEntry(content=content, timestamp=datetime.now(), tags=tags or [])
        await self.store.store(key, entry)

    async def recall(self, key: str) -> Optional[Any]:
        """Try to remember something (more reliable than me before coffee)"""
        entry = await self.store.retrieve(key)
        return entry.content if entry else None

    async def forget(self, key: str) -> None:
        """Time to let go (like my old code)"""
        await self.store.forget(key)
