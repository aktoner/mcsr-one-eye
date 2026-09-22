As an enjoyer of MCSR ranked as a spectator esport, I have recently seen a lot of arguments about sending one-eyes. To me, it was never very obvious what an optimal strategy would be because of the general variance present in ranked. That's what made me look at some data to model the situation as accurately as I could. I don't claim to have found a perfect solution, but I believe my model is fairly accurate, and I think high-level runners should employ a similar strategy to what I am suggesting if they wish to maximize their win rate. 

Skip to conclusion if you only want my thoughts on how you should play your game.


Scenario
---------
The situation I attempted to model here is the following: 
    - You are in the nether fortress, at a (cleared) spawner
    - You have 11 blaze powder
    - You just killed a cycle of freshly spawned blazes
    - Your two options are:
        +A: Stay at the fort until the next cycle of blazes spawn and kill them for another blaze rod 
        +B: Leave the fortress and hope that the end portal is a one-eye (at least 1 of the 12 eyes in the portal frame are filled by the game)
    - Your opponent was, is or will be in the same situation.

There are interesting variations of this situation that can be modelled with a similar methods but those I leave as an exercise to the reader. (Exercise: Is it ever worth to send 2 eyes?)

Some assumptions
-------
The goal of the decision of making play A vs B is to maximize your perceived probability of winning.

To model this situation I have used data from season 10s top 50 (by phase points). If you are far below this level you should probably not send one-eyes (although I invite you to run your own numbers in order to test this hypothesis).

I have modelled "being ahead when the situation occurs by T seconds" as receiving "Into Fire" T seconds before your opponent. This is because blinding is a fake split. Also, as a runner you get quite minimal useful information about your opponent between "Into Fire" and "Eye Spy", so in my opinion this guess is close to as good as the runners.

#Another somewhat reasonable but import

I discuss more technical assumptions I have made in sections ...

Results 
======
You should sometimes send a one-eye! 

If you know your opponent *isn't* sending a one-eye (e.g. you are playing vs Feinberg), you should send it if:

    - You are behind by between 1.75 and 24.35 seconds.
At most, when you are 9.8s behind, your win probability increases by 2.65% from 40.81% to 43.46%.

If you know your opponent *is* sending a one-eye (e.g. when playing ANJOUU), you should send it too if:

    - You are ahead by between 1.75 and 24.35 seconds. 

When you don't know whether your opponent is or isn't sending a one-eye it get's a bit more complicated. See the game-theretic solution below. 

Below is a graph of your estimated probability of winning. Strategy A (never sending a one-eye) in blue, and strategy B (always sending a one-eye in Orange. In both of these graphs the opponent is assumed to never send a one-eye. The value T is how far ahead you are to "Into Fire", where a negative value means you are behind. 

Game-theoretic solution
----
An optimal strategy to maximize the probability of winning is random, after reading the strategy above you can see that it's correct to be unpredictable. However, the optimal strategy is not to split 50-50, it is to follow the following graph:
This means that when you're ahead by T seconds, you should send the one-eye P(T)% of the time. (Negative value of T means you're behind).

The math behind this isn't very intuitive (atleast not to me). To get my breakdown of how this is calculated look at section...

Issues with game-theoretic solution
----




Conclusion
====
What I have tried to quantify using this analysis is the intuition that the community has agreed upon previously, the fact that if you are behind you want to do more high-risk plays that may save you time, while the player ahead should generally avoid them. I believe top runners are very aware of this fact and use it in many games.

My numbers show that you should, in fact usually (>80% of the time) send a one-eye if you are 2-24 seconds behind. Using knowledge about the seed, yourself and your opponents playstyle and skill level, you can adjust this range. 

If you are ahead by the same range, you should consider countering your opponents strategy to send it by also sending it. However, do this rarely (<20% of the time), since sending it when your opponent doesn't send it hurts your probability of winning by a lot.


