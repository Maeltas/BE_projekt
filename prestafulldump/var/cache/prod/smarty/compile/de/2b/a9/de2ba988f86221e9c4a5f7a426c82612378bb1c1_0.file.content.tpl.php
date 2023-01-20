<?php
/* Smarty version 4.2.1, created on 2022-12-18 09:55:07
  from '/var/www/html/control/themes/new-theme/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '4.2.1',
  'unifunc' => 'content_639ed56b5cd532_47914471',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'de2ba988f86221e9c4a5f7a426c82612378bb1c1' => 
    array (
      0 => '/var/www/html/control/themes/new-theme/template/content.tpl',
      1 => 1666787715,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_639ed56b5cd532_47914471 (Smarty_Internal_Template $_smarty_tpl) {
?>
<div id="ajax_confirmation" class="alert alert-success" style="display: none;"></div>
<div id="content-message-box"></div>


<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
  <?php echo $_smarty_tpl->tpl_vars['content']->value;?>

<?php }
}
}
