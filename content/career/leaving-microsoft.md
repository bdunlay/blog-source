Title: Leaving Microsoft
Date: 2015-01-21 23:38
Modified: 2015-01-21 23:38
Tags: microsoft, career,
Slug: leaving-microsoft
Summary: As of last Friday, I left my job as a software engineer at Microsoft. I am now looking ahead to joining a startup in a few weeks. This post is a rehash of my time there, and a reflection about why I left.

As of last Friday, I left my job as a software engineer at Microsoft. I am now looking ahead to joining a startup in a few weeks. This post is a rehash of my time there, and a reflection about why I left.

## My World

I worked in a group called Customer Experience Engineering, where my team essentially worked directly with Qualcomm (our chipset manufacturer and firmware provider), mobile operators (Verizon, AT&T, T-Mobile, and countless operators around the world), and device manufacturers, etc. 

The team was full of high-level engineers. The majority of folks, for the majority of my tenure, were senior and principle level. They did amazing work and I'm priviliged to have worked with and learned from them.

Our main focus was on the commercialization of new devices. That is, with each new device and each new chipset, we modified the Windows Phone OS so that it would integrate well and take advanage of new features.

One such example is the Nokia Lumia 1020 -- a 41 Megapixel camera. Our team provided special OS support to enable this device. 

Another example is adding support for quad-core devices, high resolution screens, CDMA+GSM dual SIM, etc. We also added new features such as live folders, three-tile-wide start screens, action center, quick settings, and more.

My first role was developing a web frontend as well as cloud service backends which enabled us to share our Microsoft test infrastructure with our partners (those entities mentioned previously). I'd done web before and so it became a natural role for me.

My immediate manager was, without going into details, absolutely terrible, and after almost a year, I was prepared to quit the company simply to get out of that environment.

Fortunately for me, I was introduced to a new opportunity within CXE doing systems-level development in Networking/Connectivity for the the OS. With the support of my upper management I made the switch and spend the next year and a half doing development in this area. 

## My Accomplishments

I managed to do a lot in that year and a half, and I came a long way as a developer. I joined and began brushing up on my C++ skills after doing nothing but C# (ASP.Net MVC and cloud services), JavaScript, and HTML. 

Within 6-8 months I had delivered a major feature. I developed a huge addition to the cellular stack in one of our most complicated areas (cellular manager), enabling CDMA+GSM dual SIM devices. By that time I was actively contributing to the codebase, and had became pretty good at debugging (with no prior experience to help). 

I'd also become the relative expert in the area of CMAS (emergency alerts, like Amber alerts), the cellular settings page, etc. 

I think for the time I spent there, I did a lot of big ticket items. My contributions were significant, and my responsibility and ownership vastly larger than I'd have imagined. 

My most well-known contribution was for a cellular data toggle that I added to quick settings in the action center drop down. It was the second the most requested feature by our users and had been active for a very long time, and I delievered it to much fanfare.

This was something I really wanted to deliver. It had been stagnating in the backlog for months, and  with nearly 50,000 votes on our user feedback site, the 2nd most of any feature requested, I was eager to make it happen.

My team took ownership of the feature due to lack of movement by other teams, and we effectively snuck it into the product under the rug before anyone above stop it from happening. It turned out to be contentious, with one of the directors telling me that the feature simply didn't matter and no one wanted or needed it, despite all of the evidence to the contrary, AFTER it had shipped.

One shouldn't have to take ownership from others and sneak code into a product in order to get shit done.

## My Impact

I found it extremely difficult to impact the development of the phone in ways that were meaningful to me. I thought that part of my job was to improve the user's experience in every way possible. I self-hosted our software and devices day-in and day-out, and when I found areas for improvement, I reported them.

At first, when I didn't know any better, I blasted large Windows Phone email distribution lists with the hope of finding an expert. Admittedly, this is not the most effective way to bring about change.

As time went on my attempts became more targeted and specific (filing bugs directly against the team owning the area, or emailing specific individuals responsible for the area). 

The almost universal response though seemed to be that we don't have time for this, nor do we care, in the form of **Won't Fix** or **By Design**. It seemed simply that unless there was some pressure from upper management to do something, it would absolutely never get done.

In one instance, when we released live folders on the start screen, I noticed that the user was unable to type emojis into the folder titles -- but emojis could be copied and pasted in.

I figured this was likely an oversight, and filed a bug with the relevent team. Like always, the bug was closed and ignored. I pushed back, and in doing some research into the code, found that it was only an attritbute of the XML defining the text box for the folder name that needed to be changed -- that's right, less than one line of code. So I made the change and gave the diff to the team.

They begrudgingly said they'd take the fix in a later release, but 7 months and at least 11 mini-releases later, that change has yet to see the light of day. This is of course a very small feature, but I felt that it was one [that would delight users](http://www.windowscentral.com/spice-up-your-nokia-app-folders-windows-phone-emoji) at very little cost to us. Low hanging fruit, if you will. Furthermore, all of our competitors AND Windows 8 allowed users to type emojis directly into folder or group titles. So why not us?

With each of my suggestions rejected, I found this effort to be in vain, and frankly extremely depressing over time. In a journal entry I wrote while solo-camping and soul searching at Gothic Basin in the North Cascades, I wrote:

> Influencing other teams and product decisions is like tooth-and-nail. And when it's all said and done, I feel even worse for voicing my opinions than if I had just kept my ideas to myself.

I really cared. I was passionate about the product and making things better for our customers. I really wanted to make a difference. But I could never find a way to convince other people that these details I'd find were worth their time. I came to feel like an annoyance, and it had a chilling effect on me. 

This was not the way I wanted to feel.

## Organizational Direction

Aside from my desire to impact and inability to do so, the organization took a turn for the worse through reorgnizations and plans that I was never privvy to. 

Our leadership broke up, was replaced, and then our scope and future plans dropped off of a cliff. Morale dropped to all time lows (worse than after people had been laid off two years prior). People began leaving the organization, with goodbye emails being sent several times a week as folks joined new teams. 

The only responsibilities left for us was to port our previous year and a half's work into Windows 10, manually, due to incompatibilities with our new development tools and environments.

All of the hope we'd had as a group to make Windows Phone the best we possibly could evaporated. 

## Final Days and Next Steps

My skip-level manager pulled me aside the day before I told him that I was going to leave the company, and he asked what was wrong. He told me I wasn't smiling anymore, which had been one of my shining traits in earlier days. I tried to play it off, but he didn't buy it. That's how obvious my internal conflict was.

All of this felt damaging to me and my personality. I wasn't thriving. I was depressed, deflated, uninspired, and unmotivated. I decided to take charge of my own career and my own life and do something that I wanted to do. 

So I left. 

I chose a startup because I think that there I can have the impact I want. Everyone who matters will be in the same room as me, and I'll be able to, at a minimum, let my ideas and concerns be heard and acknowledged, rather than dismissed and ignored. I want my passions to be reignited and fueled rather than suppressed and extinquished, and I think this new opportunity will help me do that. 