<%inherit file="/base.mako" />

<%def name="head_tags()">
  
</%def>

<form action='/login' method='post'>

Email: <input type="text" name="email" /><br/>
Password: <input type="password" name="password" /><br/>
<input type="submit" value="login" />
</form>

${c.login}