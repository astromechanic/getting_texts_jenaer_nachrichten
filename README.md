As the learner of German, I decided to write a code that would help me to learn German vocabulary. I am also interested in local news that are written in German. My aim was to create a corpus of news from the Jenaer Nachrichten in order to find out what vocabulary I should learn at first in order to understand more.

This repository contains a code written in Python (ver. 3.5.2) and .txt files.

<b>getting_texts_jenaer_nachrichten.py</b>

This code creates a corpus of the texts from the Jenaer Nachrichten. A user can decide how many texts should be downloaded. The more texts are downloaded, the more representative is the corpus. 

The code creates three .txt files: <br>
<b>html.txt</b> — the content of every single web page<br>
<b>raw_texts.txt</b> — the fragments with the texts from a web page containing some tags<br>
<b>clean_texts.txt</b> — the texts free from the tags etc. This is the final file that is used later.<br>

The file <b>clean_texts.txt</b> was then processed with AntConc (the freeware corpus analysis toolkit http://www.laurenceanthony.net/software/antconc/) in order to create a list of words ordered by frequency and 3-Grams. 

The frequency list allows to learn first the words that are more frequent in the text, and thus helps to understand more texts faster. It begins obviously with the most frequent German words at all, such as <i>der, die, und</i> etc. But then one can find more sophisticated words like <i> Verfügung, Möglichkeit</i> and <i>anschließend</i>. 

To my mind, the more applicable thing is the list of 3-Grams which has two possible uses. 
<ul>
<li>First, it enables to understand what the local news are about. For example, the most frequent 3-Grams in my set of news are the following: fc carl zeiss, carl zeiss jena, ff usv jena, den chemnitzer fc. Therefore, we can conclude that the football topic is more represented now than, let's say, the coronavirus.</li>
<li>Second, it is useful to learn the words right away with grammar and context, for example: not only <i>Donnerstag</i> but <i>am Donnerstag</i>, not only <i>Motto</i> but <i>unter dem Motto</i>, not only <i>Holzmarkt</i> but <i>auf dem Holzmarkt</i> and so on.</li>
</ul>

This approach though has some limitations. When the phrases (2-Grams or 3-Grams) are extracted from the text, they lose 
the broader context. That can lead to confusion: there are some chunks like <i>der polizei jena</i> and one can think that the word "Polizei" is masculine, which is not. 

Anyway, it could be a useful tool to learn a language from real texts.
