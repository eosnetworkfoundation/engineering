# Strawman for ENF Release Support Schedule

**ENF_Soft** : ENF produced products leap/cdt/etc.

**Cardinal release** : A release that impacts interfaces, APIs or consensus (host function additions, new account system, etc).

**Marginal release** : A release that adds new functionality in an additive manner that impact consensus or have major impacts to downstream users (i.e. ship protocol changes, etc.).

---

## Support window:


Assuming that: 

> *ENF_Soft vW.0.0* is a **cardinal release** <br>
> *ENF_Soft vX.0.0* is a **marginal release** <br>
> *ENF_Soft vY.0.0* is a **cardinal release** <br>
> *ENF_Soft vZ.0.0* is a **marginal release** <br>

Then,

> We will support *ENF_Soft vW.0.0* and *ENF_Soft vX.0.0* if we are releasing vX.0.0. <br>
> We will support *ENF_Soft vY.0.0* if we are releasing vY.0.0. <br>
> We will support *ENF_Soft vY.0.0* and *ENF_Soft vZ.0.0* if we are releasing vZ.0.0. <br>

Or more succinctly, 

$$ DoesSupport(v) = \left\{\begin{array}{ c l }\{v-1, v\} & \quad \textrm{if } v \in \textrm{MarginalReleases} \\ 
                           \{v\} & \quad \textrm{otherwise} \end{array} \right. $$


So,

Let’s say:
 
v1.0.0 is a *cardinal release*

v2.0.0 is a *marginal release*

v3.0.0 is a *cardinal release*

v4.0.0 is a *marginal release*

Then,

> DoesSupport(1) -> {1} , we should support v1.0.0 <br>
> DoesSupport(2) -> {1, 2}, we should support v1.0.0 and v2.0.0 <br>
> DoesSupport(3) -> {3}, we should support v3.0.0 <br>
> DoesSupport(4) -> {3, 4}, we should support v3.0.0 and v4.0.0 <br>

--- 

## What about Release Candidates? 
 
The proposed solution would be to augment the above to subsume release candidates until they are final.  The above defines the end support after releases have gone final.  There are questions around do we want to gate that until consensus upgrade for cardinal releases?  I propose that we do. 
 <br>

So,
 
*DoesSupport(v)* would become the following: 
 
 $$ DoesSupport(v) = \left\{\begin{array}{ c l }\{v-1, v\} & \quad \textrm{if } v \in \textrm{MarginalReleases} \\ 
                           DoesSupport(v-1) \cup {v} & \quad \textrm{if } v \in \textrm{CardinalReleases} \land v \in \textrm{ReleaseCandidates} \\
                           \{v\} & \quad \textrm{otherwise} \end{array} \right. $$

So,
 
DoesSupport(1) -> {1} the same no matter what
DoesSupport(2) -> {1, 2} same as before

DoesSupport(3) -> {3} When v3.0.0 is out of RC or {1, 2, 3} When v3.0.0 is still in RC

DoesSupport(4) -> {3, 4} same as before
