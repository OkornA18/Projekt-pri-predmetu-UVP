% rebase("views/base.tpl")

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