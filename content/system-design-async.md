Title: System Design Primer: Asynchronism
Date: 2020-01-13
Status: draft
Summary: Asynchronism
CoverImage: http://i.imgur.com/6SbxQah.png
Thumbnail: http://i.imgur.com/oCWLuMC.png

## Asynchronism

<p align="center">
  <img src="http://i.imgur.com/54GYsSx.png"/>
  <br/>
  <i><a href=http://lethain.com/introduction-to-architecting-systems-for-scale/#platform_layer>Source: Intro to architecting systems for scale</a></i>
</p>

Asynchronous workflows help reduce request times for expensive operations that would otherwise be performed in-line.  They can also help by doing time-consuming work in advance, such as periodic aggregation of data.
