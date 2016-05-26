Title: Open Source Collaboration
Date: 2015-01-27 10:15
Modified: 2015-01-27 10:15
Tags: github, open source, collaboration, hacking, python, iot
Slug: open-source-collaboration
Summary: Recently, I've started collaborating on some open-source projects. It's the first time I've ever ventured into the world of collaborative software development outside of a professional or academic setting, and it's really fun!

Recently, I've started collaborating on some open-source projects. It's the first time I've ever ventured into the world of collaborative software development outside of a professional or academic setting, and it's really fun!

## Wireless Lightbulbs

It all started when I bought some wireless lightbulbs. They come with a gateway (which runs Linux) that runs a local server through which a mobile app can issue commands to the bulbs. 

Of course, using a mobile app to control your lightbulbs is insane. It's way easier and faster to use a switch on the wall.

I started digging and found some resources for node.js and python. Other enthusiasts had begun to control the bulbs and even added their own features on top (e.g. sunrise) via their unofficial APIs.

I began developing further the python module, and was soon invited to collaborate with the python dev. Things were silent and stable for a few months.

## Breaking Update, Community to the Rescue

The company that sells the gateway decided to push a "security update" out of the blue one day, and ended up breaking everyone's DIY projects. I was pretty upset at first (they'd broken my sunrise, taken away root access, and done it all without my permission). I called and then sent a follow up email, but they seem to have ignored me for the most part.

Once I got over myself, I began searching Twitter and found that the node.js library had been updated recently -- following that trail, I discovered that the developer had reverse engineered the new protocol and was able to make his library work again. 

With the explanations on his blog, I was able to patch the python library and am back up and running again.

I've been emailing with the developer of the python library and the developer of the node.js library, discussing features, reverse engineering techniques, etc, and it's been awesome to push these parallel projects farther along. 

## Coding Under the Microscope

It's a little scary putting my code out there for others to see (and I will be the first to say I'm a little weary of what I've contributed so far). It feels personal, much like writing this blog. People can see how I think, are easily able to criticize my ideas, and (oh no!!) might form some opinions about me and my intellectual abilities. That's a little scary. 

But then again... who cares? It's a good exercise for me to make myself vulnerable and do something that scares me. Criticism and feedback will help me grow.

And even if the code is terrible at first, at least I'm doing it rather than not. As time goes on and with more eyeballs, things will improve. That's how the learning process goes. The point of these projects isn't to be perfect, but to make something, learn something, and have fun doing it. So far I am achieving these goals!

You can check out my first real collaborate project on github at [http://github.com/therivenman/pygop](http://github.com/therivenman/pygop).