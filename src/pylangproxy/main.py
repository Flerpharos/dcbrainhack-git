from __future__ import annotations

from typing import Iterable


class LangProxyValue[T]:
    pass


class LangProxyLoopDef:
    pass


class LangProxyBranchDef:
    pass


class LangProxy[T]:
    def __init__(self):
        pass

    def __setattr__(self, key: str, value: T) -> None:
        raise NotImplementedError

    def __getattr__(self, key: str) -> LangProxyValue[T]:
        raise NotImplementedError

    def range(
        self,
        start: int | LangProxyValue[int],
        stop: int | LangProxyValue[int],
        step: int | LangProxyValue[int] = 1,
    ) -> Iterable[LangProxyValue[int]]:
        raise NotImplementedError

    def define(
        self, name: str, *args: str
    ) -> LangProxyFuncDef[T]:
        raise NotImplementedError

    def breakloop(self) -> None:
        raise NotImplementedError

    def continueloop(self) -> None:
        raise NotImplementedError

    def loop_until(self, cond: LangProxyValue[bool]) -> LangProxyLoopDef:
        raise NotImplementedError

    def branch_if(self, cond: LangProxyValue[bool]) -> LangProxyBranchDef:
        raise NotImplementedError

    # WHILE, IF


class LangProxyFuncDef[T](LangProxy):
    pass

vizzy = LangProxy()
vizzy.y = (1, 2, 3)
vizzy.x = (2, 3, 4)

for i in vizzy.range(1, 2):
    vizzy.x += i

with vizzy.define("func_name", "arg1", "arg2") as func:
    func.y = (1, 2, 3)
    with vizzy.loop_until(func.y.x < 10):
        func.
    func.ret