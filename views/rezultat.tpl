% rebase("Projekt-pri-predmetu-UVP-master/views/base.tpl")

<div align="center" style="background:#FFDAB9">
<p>Rezultat:</p>
  <h1>
  <table class="center">
%   for vrstica in rezultat:
      <tr>
      <td>{{ vrstica }}</td>
      </tr>
% end
  </table>
  </h1>
  </div>
  
<div align="right">
  <a href="/" class="btn btn-outline-secondary" role="button" aria-pressed="true">Domov</a>
</div>