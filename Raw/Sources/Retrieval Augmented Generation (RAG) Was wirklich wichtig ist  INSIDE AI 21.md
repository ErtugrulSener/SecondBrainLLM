---
Title: "Retrieval Augmented Generation (RAG): Was wirklich wichtig ist | INSIDE AI #21"
Author: "Fraunhofer IEM"
Reference: "https://www.youtube.com/watch?v=jZoyg74ZyqM"
ContentType:
  - "markdown"
Created: 2026-07-18
Processed: true
tags:
  - "source"
---
![](https://www.youtube.com/watch?v=jZoyg74ZyqM)

Retrieval Augmented Generation (RAG) galt 2024 als eines der wichtigsten Konzepte zur Verbindung von LLMs mit externem Wissen. 2025 steht es nicht mehr im Rampenlicht – zu Unrecht? In dieser Folge analysiert KI-Experte Tommy Falkowski, warum RAG auch heute noch eine zentrale Rolle spielt, wenn es um aktuelle Informationen, begrenzte Kontextfenster und semantische Suche geht. Es geht um Embeddings, hybride Suchmechanismen und den praktischen Einsatz im Unternehmenskontext.

Überblick
0:00 – Einstieg & Rückblick
0:27 – RAG vs. neue Trends
1:00 – Grenzen von LLMs
2:05 – Prompt Engineering
3:01 – Lücken im Training
3:25 – RAG einfach erklärt
4:05 – Datenflut in Unternehmen
4:37 – Relevanz statt Masse
5:06 – Embeddings verstehen
5:58 – Semantische Suche
7:16 – Rechenaufwand
7:56 – Websuche als Tool
8:39 – RAG im Unternehmen
9:11 – Praxis & Formate

🎙 Mit dabei: Tommy Falkowski https://www.linkedin.com/in/tommy-falkowski/

Mehr erfahren & vernetzen:
🔗 LinkedIn: https://www.linkedin.com/company/fraunhofer-iem
📸 Instagram: https://www.instagram.com/fraunhofer.iem
📩 Newsletter: https://www.iem.fraunhofer.de/newsletter

Abonniere unseren YouTube-Kanal: https://www.youtube.com/@UCcYK2VMK5ts0MDSy0kaxdSw

#KI #RAG #LLMs

## Transcript

### Introduction & review

**0:00** · Hello and welcome to Inside AI.

**0:03** · Today we’re talking about Retrieval Augmented Generation, or RACKT for short.

**0:15** · Yes, the RAG topic isn’t all that new anymore.

**0:18** · You will probably also say, Tommi, it is already in the year 2025, Now you come around the corner with RACKT.

**0:23** · That was the hype last year.

**0:25** · It's old hat.

**0:26** · We now have agent systems, agentic search, etc.

### RAG vs. new trends

**0:30** · And long context windows of a million and sometimes even more.

**0:34** · RACKT doesn’t play any role anymore.

**0:37** · Yes and no.

**0:38** · Well, of course it's not quite that simple.

**0:40** · And that is why it is still worth thinking about it today, how to address the topic of retrieval, That is actually the core point here, namely gathering relevant information in combination with generative AI.

### Limitations of LLMs

**1:00** · And to understand this, let’s just take a quick look again, how the mechanism in an LLM works, namely the so-called context window.

**1:10** · That means an LLM, which I have already explained in some parts in the previous episodes, each LLM has a fixed context window, i.e. a maximum number of tokens or words it can process.

**1:26** · And if you want to process something with longer, with more tokens, then you just have to cut something off somewhere in the front or back in the middle.

**1:35** · And there are now models that can process up to one million tokens, for example Gemini 2.5 Pro from Google.

**1:44** · The problem is still, that just because a model has a context window of, for example, one million tokens, that does not mean that it can handle these many tokens just as well, like with fewer tokens.

**1:56** · So the fewer tokens I give the model, the better the quality can be.

**2:04** · And that means that what input I give to the model is crucial.

### Prompt engineering

**2:09** · When we think about prompt engineering, This is basically the user prompt that is given to the model.

**2:16** · This is an essential component in working with these generative models, based on LLMs.

**2:21** · We also always have a system prompt, which is now specified by the AI labs in the case of chats GPT or Anthropic.

**2:30** · In the case of Cloud 4, for example, the system prompt is, I believe, 60,000 characters long.

**2:36** · So a very, very long system prompt.

**2:40** · And so you still have to manage this context window a bit.

**2:47** · And now the question arises: what options do I have to improve my system?

**2:54** · For example, if I want to have current information.

**2:57** · A model is always trained with a dataset.

**3:00** · And if I were to operate only this bare model, then the model cannot show me any events, which were not yet included in the training dataset, because the model simply does not know them, has never seen them.

### Gaps in training

**3:13** · This means we need to create an interface with which the system can, so to speak, extract this information.

**3:20** · And that’s where the topic of retrieval augmented generation comes into play.

**3:24** · Because, to put it simply, it means nothing else, than taking information from any source and transfer it to the context window of our LLM.

### RAG explained simply

**3:38** · We can now call the whole topic here external information and in the simplest case we then put the whole thing into our context window, in principle included in our actual user prompt.

**3:54** · And of course for smaller text sources, if we have a PDF for example, If it is not too long and contains mainly text content, it is sufficient.

**4:04** · We can copy and paste it or, as with Chat GPT, simply upload the PDF and the model can simply process the entire text.

### Data flood in companies

**4:14** · But if we look at this in reality, for example in companies, We have tons of data, tons of textual data and other data, Tons of information.

**4:25** · And if I now want to get an answer to a very specific question, in the corporate context, for example, then I can't just take all the data we have and load it into the context window.

**4:36** · This simply doesn't work because there is simply too much data.

### Relevance instead of mass

**4:41** · And even if it did fit, it wouldn’t necessarily improve the quality, because a lot of the information that I then give to the model, is not at all relevant to the request I am making.

**4:52** · This means that you must have a mechanism to identify relevant information and then load it into the context window as needed.

**5:05** · And a mechanism that has actually been very hyped in the last two years, is the topic of so-called embeddings.

### Understanding embeddings

**5:15** · RAC is often equated with embeddings, but this is simply wrong, because it is just a kind of information identification mechanism.

**5:27** · And with embeddings, it is actually a technology that has been used for a long time, whenever it came to so-called semantic search.

**5:36** · In the semantic search, unlike the keyword search, where I searched for individual words and whenever this word appears in a source text, the corresponding source text is shown to me.

**5:47** · With a semantic search, you can work with similarities.

**5:51** · This means I can enter a search query and similar results will be displayed.

**5:57** · In principle, this is no different than a Google search.

### Semantic search

**6:00** · Behind Google Search is Google's Knowledge Graph, and this Knowledge Graph also works with these embeddings, among other things.

**6:09** · And in principle, to put it simply, it is simply a mathematical representation of content.

**6:15** · You essentially encode text sections into numbers and can then calculate similarities.

**6:23** · So you can say how similar two sentences are to each other, for example.

**6:27** · This is essentially a mathematical calculation that is carried out.

**6:31** · And this similarity is then given to me in the form of a number.

**6:35** · And if I now want to identify information in my entire knowledge base, in the company for example, then it might be a good idea to actually work with these embeddings.

**6:46** · This has the advantage that I no longer have to search only using keywords, but can also perform these semantic searches.

**6:53** · This means that I do not need to know exactly which terminology was used in the document or section I am looking for, but it is enough if I formulate something that simply has a high similarity to this text.

**7:06** · The disadvantage of using this system is that these embeddings have to be calculated.

**7:12** · This means that this is a computationally intensive task.

**7:15** · All the text that you want to store in this embeddings database must first be transferred.

### Computing effort

**7:23** · And every time I store new information in whatever text format, I have to calculate additional embeddings.

**7:30** · This means that there is a continuous, additional computational effort that is added.

**7:36** · This is also the reason why semantic search alone is not always the key to the goal or the right way.

**7:43** · There are also approaches where you can sometimes achieve even better results with a simple keyword search than with embeddings alone.

**7:51** · In practice, it is always a combination of many different approaches.

### Web search as a tool

**7:56** · And finally, if we use ChatGPT for example and ChatGPT performs a web search in the background, Ultimately, it is nothing more than a type of mechanism for information extraction, essentially a retrieval mechanism.

**8:14** · And what's becoming increasingly clear lately is that these models are very good at using tools.

**8:23** · Tools that are defined by AI labs, such as web search.

**8:27** · But also tools that we then connect to the LLMs using the MCP protocol, for example.

**8:33** · I already made a video about this. Feel free to watch it again if you'd like to learn more.

### RAG in companies

**8:39** · And that is also the reason why Retrieval Augmented Generation continues to be important.

**8:45** · Maybe the term is a little worn out.

**8:48** · Nevertheless, we still need information retrieval.

**8:51** · And that is often actually the key to making these technologies usable and effective in a corporate context.

**8:59** · Because if the model cannot identify the relevant information that I need for my query, it won't be able to give me a good answer either.

**9:08** · And that's why we're working very hard on it.

**9:10** · We have already implemented various solutions in various projects in the context of retrieval augmented generation.

### Practice & formats

**9:19** · And as I said, it is usually the combination of many different data sources that are connected.

**9:26** · These can also be SQL databases, for example, where searches are then carried out using the structured data.

**9:33** · And here it is important to think early on about the best possible formats that you want to store.

**9:40** · PDFs, for example, are naturally found in many companies.

**9:43** · However, this is not necessarily the best format because it is actually not very standardized.

**9:49** · It is very tedious to extract, for example, only the text and images separately from a PDF and then describe the images.

**9:57** · Of course, there are different providers and mechanisms that do this.

**10:00** · However, I would say it is unnecessary.
