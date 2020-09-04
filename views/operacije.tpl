% rebase("views/base.tpl")

<form action={{ operacija }} method="POST">
  <div class="form-group">
  <table class="center">
  
  <tr>
    <td>
    <h3><label for="matrika1">Vpiši prvo matriko:</label></h3>
    <textarea class="form-control" id="matrika1" rows="10" name="matrika1" placeholder="prva kvadratna matrika"></textarea>
    </td>
    <td>
    </td>
    <td>
    <div align="center">
      <h1>{{ operator }}</h1>
    </div>
    </td>
    <td>
    </td>
    <td>
    <h3><label for="matrika2">Vpiši drugo matriko:</label></h3>
    <textarea class="form-control" id="matrika2" rows="10" name="matrika2" placeholder="druga kvadratna matrika"></textarea>
    </td>
  </tr>
  <tr>
    <input type="submit" value={{ operiraj }}>
  </tr>
  </table>  
  </div>
</form>