Title: Tableau 9 Features: Initial Impressions from Beta
Date: 2015-03-24
Summary: With the final beta in the hands of testers, I thought I'd write up a review of my favorite features in Tableau 9.
Tags: Data
CoverImage: https://raw.githubusercontent.com/donnemartin/donnemartin.github.io/master/images/posts/tableau2_cover.jpg
Thumbnail: http://i1.wp.com/donnemartin.net/wp-content/uploads/2014/09/tableau2_cover.jpg?zoom=2&resize=320%2C202

With the final beta in the hands of testers, I thought I would give a quick overview of my favorite features in Tableau 9.

## First Impressions

When opening up Tableau, users are now welcomed with a revamped screen:

<p align="center"><img src="http://donnemartin.net/wp-content/uploads/2015/03/tableau_welcome1.png" alt="" class="img-responsive"/></p>

The initial screen has great flow from left (start here) to middle (do work) to right (learn more).  The new "Discover" section in particular is a great addition for newcomers and seasoned users alike, and has led me to view some great content on Tableau public such as the [London Cycle Hire Usage](https://public.tableau.com/s/gallery/london-cycle-hire-usage?edition=pro&version=9.0):

<p align="center"><img src="http://donnemartin.net/wp-content/uploads/2015/03/tableau_viz1.png" alt=""  class="img-responsive"/></p>

## Improved Speed and Streamlined Workflows

A major focus area for Tableau 9 revolves around improved application speed.  In general Tableau 9 feels snappier.  Application startup, loading dashboards, and executing complex queries all seem faster.

Closely related to speed of the program is the improved efficiency users get from various workflow-streamlining features.  Less time waiting for Tableau to crunch calculations coupled with the reduced need to wrestle suboptimal workflows means more opportunities to focus on what matters.

The level of detail and data prep capabilities seem to be the focus of many Tableau 9 articles.  [Level of detail](http://www.tableau.com/about/blog/2015/2/introduction-level-detail-expressions-36655) allows you to easily analyze data at multiple aggregation levels:

<p align="center"><img src="http://donnemartin.net/wp-content/uploads/2015/03/tableau_lod.png" alt="" class="img-responsive"/></p>

Improved [data prep](http://www.tableau.com/about/blog/2015/1/tableau-90-auto-data-prep-stay-flow-35980) could reduce some of my data wrangling time in Pandas or R before inputting it to Tableau:

<p align="center"><img src="http://donnemartin.net/wp-content/uploads/2015/03/tableau_pivot.png" alt="" class="img-responsive"/></p>

I appreciate that Tableau seems to be moving away from modal dialogs that block screen real estate and interrupt my train of thought.  The Analytics palette, calculation editor, and pill calculations all keep my focus on the main document window rather than juggling from dialog to main window.  The autocomplete feature is handy as it helps prevent me from having to toggle between palettes or help docs.

<p align="center"><b>Analytics Palette</b></p>
<p align="center"><img src="http://donnemartin.net/wp-content/uploads/2015/03/Tableau_analytics.png" alt="" class="img-responsive"/></p>
<p align="center"><b>Pill Calculations</b></p>
<p align="center"><img src="http://donnemartin.net/wp-content/uploads/2015/03/Tableau_pill.png" alt="" class="img-responsive"/></p>
<p align="center"><b>Calculation Editor</b></p>
<p align="center"><img src="http://donnemartin.net/wp-content/uploads/2015/03/Tableau_calc.png" alt="" class="img-responsive"/></p>

Tooltips now update quickly as your mouse moves.  Previously I had to pause mouse movement for Tableau to update the tooltip.  In some situations I would sometimes have to move the mouse completely out of a viz then move it back for the tooltip to update.  Another handy improvement is a tooltip shown when you hover over a tab name:

<p align="center"><img src="http://donnemartin.net/wp-content/uploads/2015/03/Tableau_tooltip.png" alt="" class="img-responsive"/></p>

Bonus: the filmstrip mode now shows both titles and images, preventing the need to frequently swap from filmstrip mode to tab mode.

A relatively low-key yet useful addition is the Hide/Unhide All Sheets feature, as managing sheet hiding in prior versions was quite difficult:

<p align="center"><img src="http://donnemartin.net/wp-content/uploads/2015/03/Tableau_unhide.png" alt="" class="img-responsive"/></p>

## Bug Fixes and Improved Stability

Being a Mac user, one of my biggest gripes was the 'bouncing' Tableau icon on the dock whenever I kicked off a long operation and switched to another application.  This was a huge distraction and forced me to schedule lengthy operations such as data extract refreshes during my lunch break or after hours.  A later iteration of Tableau 8.x was advertised to have fixed this issue, but it was still present on my machine (MBP Retina, OSX 10.9.5).  I am happy to report this is no longer present in Tableau 9.

<p align="center"><img src="http://donnemartin.net/wp-content/uploads/2015/03/Tableau_icon.png" alt="" class="img-responsive"/></p>

In addition to story points now being customizable, it seems they have become more robust.  For example, after several lockups, I made it a habit to save prior to doing a drag and drop to change story points ordering.  I have yet to encounter these problems in the latest version.

## Conclusion

With Tableau 8 introducing great features such as 64 bit support, native OSX support, and R integration, I figured the Tableau team had their work cut out for them with the next release.  I applaud the Tableau team's improvements to application speed, streamlined workflows, and increased stability in Tableau 9, as focusing on these areas acts as a force multiplier to its great and rapidly growing feature set.