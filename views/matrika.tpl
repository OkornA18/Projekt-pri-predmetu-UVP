% rebase(""views/base.tpl"")

<form action={{ potek }} method="POST">
  <div class="form-group">
    <h3><label for="matrika">Vpiši matriko:</label></h3>
    <textarea class="form-control" id="matrika" rows="10" name="matrika" placeholder="matrika"></textarea>
    <input type="submit" value={{ kar_racunam }}!>
  </div>
</form>