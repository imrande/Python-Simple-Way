# MRO Algorithm

class A: pass
print(A.mro()) # A, Object
class B: pass
print(B.mro()) # B, Object
class C: pass
print(C.mro()) # C, Object
class D(A, B): pass
print(D.mro()) # D, A, B, Object
class E(B, C): pass
print(E.mro()) # E, B, C, Object
class F(D, E, C): pass
# only consider immediate parent -> E(D) -> F, D(A, B) -> F, D, A
print(F.mro()) # F, D, A, E, B, C, Object

print()
# another example
class M: pass
class N: pass
class O: pass
class P(M, N): pass
class Q(M, O): pass
class R(P, Q): pass
print(R.mro()) # -> R, P, Q, M, N, O, Object