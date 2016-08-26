Title: Tmux Troubles
Date: 2016-8-26 13:28
Tags: programming, development, linux, tmux
Slug: tmux-trouble

I had a problem working with tmux recently. Whenever I started a new session, loads of environment variables were set which put me in some sort of zombie land. They were close but not quite right for what I actually needed set for my development environment.

Even if I closed all sessions, the environment would be restored. I checked my standard non-tmux environment, and the variables weren't set, but there they were every time I started a new session.

I commented out my `.bashrc`, `.bash_profile`, and `.profile` for good measure -- and then even renamed them out of pure irrational superstition.

I set a variable in my local environment, launched a session, and there it was. Logged out completely and launched a new session, and the variable was gone. 

## Debugging

I logged into a new machine to check the environment of a new session there. It was fine. 

I logged into the original machine using Terminal instead of iTerm2. It was broken.

This led me to believe the problem is solely isolated to tmux on a single machine. I checked for config files, any kind of state, but couldn't find anything at all. 

So I opened up the man page and started to read about the environment.

```
ENVIRONMENT

     When the server is started, tmux copies the environment into the global
     environment; in addition, each session has a session environment.  When a
     window is created, the session and global environments are merged.  If a
     variable exists in both, the value from the session environment is used.
     The result is the initial environment passed to the new process.

```

AH HA. When a tmux *server* starts, it copies the environment into the global tmux environment, and then merges that with your local environment at the time of launching a new session!

I must have accidentally started the tmux server while my development environment was set in the past, which then transferred my environment into the tmux global environment.

## The fix?

I could unset all of the environment variables one by one, but it seemed much easier to just re-start the tmux server.

`tmux stop-server && tmux start-server`

Fixed! I hope this helps somebody down the line!
