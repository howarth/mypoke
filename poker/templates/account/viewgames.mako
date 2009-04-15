<%inherit file="/base.mako" />

<%def name="head_tags()">
  
</%def>
<h2>Your Games</h2>
% for g in c.games:
 <a href="/game/${g.id}">${g.name}</a><br/>
% endfor