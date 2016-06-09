Title: SAWS Now on GitHub!
Date: 2015-09-20
Summary: Interactive command line interface that aims to supercharge the AWS CLI with features focusing on improving ease-of-use and increasing productivity. Under the hood, SAWS is powered by the AWS CLI and supports the same commands and command structure.
Tags: GitHub
CoverImage: http://i0.wp.com/donnemartin.net/wp-content/uploads/2015/09/saws.png?zoom=2&fit=1708%2C1252
Thumbnail: http://i0.wp.com/donnemartin.net/wp-content/uploads/2015/09/saws.png?zoom=2&resize=320%2C202

I've published SAWS: A Supercharged AWS Command Line Interface (CLI) on [GitHub](https://github.com/donnemartin/saws).
<h1>SAWS</h1>
<a href="https://camo.githubusercontent.com/2af72023269b0b320adf4ec55576435f5c8b79c4/687474703a2f2f692e696d6775722e636f6d2f767a43357a6d412e676966" target="_blank"><img src="https://camo.githubusercontent.com/2af72023269b0b320adf4ec55576435f5c8b79c4/687474703a2f2f692e696d6775722e636f6d2f767a43357a6d412e676966" alt="" data-canonical-src="http://i.imgur.com/vzC5zmA.gif" class="img-responsive"/></a>

<a href="https://travis-ci.org/donnemartin/saws"><img src="https://camo.githubusercontent.com/c1d6d1e8f7cdac1e6a82bf900832bbbe52d61e95/68747470733a2f2f7472617669732d63692e6f72672f646f6e6e656d617274696e2f736177732e7376673f6272616e63683d6d6173746572" alt="Build Status" data-canonical-src="https://travis-ci.org/donnemartin/saws.svg?branch=master" /></a> <a href="http://saws.readthedocs.org/en/latest/?badge=latest"><img src="https://camo.githubusercontent.com/41afe5f96e9f915ecd9706bdc7dfd19518eaf05a/68747470733a2f2f72656164746865646f63732e6f72672f70726f6a656374732f736177732f62616467652f3f76657273696f6e3d6c6174657374" alt="Documentation Status" data-canonical-src="https://readthedocs.org/projects/saws/badge/?version=latest" /></a> <a href="https://gemnasium.com/donnemartin/saws"><img src="https://camo.githubusercontent.com/11e16ba1560f0232928945436bf86340615d85ae/68747470733a2f2f67656d6e617369756d2e636f6d2f646f6e6e656d617274696e2f736177732e737667" alt="Dependency Status" data-canonical-src="https://gemnasium.com/donnemartin/saws.svg" /></a> <a href="https://codecov.io/github/donnemartin/saws/saws"><img src="https://camo.githubusercontent.com/e24a50e9dd63768d90d26a9f6be1cf3d0c3b0230/68747470733a2f2f696d672e736869656c64732e696f2f636f6465636f762f632f6769746875622f646f6e6e656d617274696e2f736177732e737667" alt="Codecov" data-canonical-src="https://img.shields.io/codecov/c/github/donnemartin/saws.svg" /></a>

<a href="http://badge.fury.io/py/saws"><img src="https://camo.githubusercontent.com/818edda38216a62a4bb36557372877febec35086/68747470733a2f2f62616467652e667572792e696f2f70792f736177732e737667" alt="PyPI version" data-canonical-src="https://badge.fury.io/py/saws.svg" /></a> <a href="https://pypi.python.org/pypi/saws/"><img src="https://camo.githubusercontent.com/04574f61c5dff98734bd6a013cc9217b9a428e47/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f736177732e737667" alt="PyPI" data-canonical-src="https://img.shields.io/pypi/pyversions/saws.svg" /></a> <a href="http://www.apache.org/licenses/LICENSE-2.0.html"><img src="https://camo.githubusercontent.com/8bf81d4b6a63eaf6f712e3092fe7238f8716e615/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6170616368652d626c75652e737667" alt="License" data-canonical-src="http://img.shields.io/:license-apache-blue.svg" /></a>
<h2><a id="user-content-motivation" class="anchor" href="https://github.com/donnemartin/saws#motivation"></a>Motivation</h2>
<h3><a id="user-content-aws-cli" class="anchor" href="https://github.com/donnemartin/saws#aws-cli"></a>AWS CLI</h3>
Although the <a href="https://github.com/aws/aws-cli">AWS CLI</a> is a great resource to manage your AWS-powered services, it's <strong>tough to remember usage</strong> of:
<ul>
    <li>50+ top-level commands</li>
    <li>~1400 subcommands</li>
    <li>Countless command-specific options</li>
    <li>Resources such as instance tags and buckets</li>
</ul>
<h3><a id="user-content-saws-a-supercharged-aws-cli" class="anchor" href="https://github.com/donnemartin/saws#saws-a-supercharged-aws-cli"></a>SAWS: A Supercharged AWS CLI</h3>
<code>SAWS</code> aims to <strong>supercharge</strong> the AWS CLI with features focusing on:
<ul>
    <li><strong>Improving ease-of-use</strong></li>
    <li><strong>Increasing productivity</strong></li>
</ul>
Under the hood, <code>SAWS</code> is <strong>powered by the AWS CLI</strong> and supports the <strong>same commands</strong> and <strong>command structure</strong>.

<code>SAWS</code> and <code>AWS CLI</code> Usage:
<pre>aws command subcommand [parameters] [options]
</pre>
<code>SAWS</code> Features:
<ul>
    <li>Auto-completion of:
<ul>
    <li>Commands</li>
    <li>Subcommands</li>
    <li>Options</li>
</ul>
</li>
    <li>Auto-completion of resources:
<ul>
    <li>Bucket names</li>
    <li>Instance ids</li>
    <li>Instance tags</li>
    <li><a href="https://github.com/donnemartin/saws/blob/master/(#todo-add-more-resources)">More coming soon!</a></li>
</ul>
</li>
    <li>Syntax and output highlighting</li>
    <li>Customizable shortcuts</li>
    <li>Contextual help</li>
</ul>
<code>SAWS</code> is available for Mac, *nix, and <a href="https://github.com/donnemartin/saws#windows-support">Windows</a>.
<hr class="featurette-divider">
<iframe src="https://ghbtns.com/github-btn.html?user=donnemartin&amp;repo=saws&amp;type=star&amp;count=true&amp;size=large" width="160px" height="30px" frameborder="0" scrolling="0"></iframe><iframe src="https://ghbtns.com/github-btn.html?user=donnemartin&amp;repo=saws&amp;type=fork&amp;count=true&amp;size=large" width="158px" height="30px" frameborder="0" scrolling="0"></iframe><iframe src="https://ghbtns.com/github-btn.html?user=donnemartin&amp;type=follow&amp;count=true&amp;size=large" width="270px" height="34px" frameborder="0" scrolling="0"></iframe>
