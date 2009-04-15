<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="/css/base.css" />
    <script src="/js/jquery.js" language="javascript" type="text/javascript"></script>
    <script src="/js/functions.js" language="javascript" type="text/javascript"></script>
    ${self.head_tags()}
  </head>
  <body>
    <div id="site">
      <div id="banner">
	<div class="logo">MyPokerStatus</div>
	<div class="links">
	<ul>
	  <li><a href="/">Home</a></li>
	  <li><a href="/login">Login</a></li>
	  <li><a href="/logout">Logout</a></li>
	  <li><a href="/account">Account</a></li>
	</ul>
	</div>
	<div style="clear:both"></div>
      </div>
      <div id="content">
	${self.body()}
      </div>
    </div>
  </body>
</html>
