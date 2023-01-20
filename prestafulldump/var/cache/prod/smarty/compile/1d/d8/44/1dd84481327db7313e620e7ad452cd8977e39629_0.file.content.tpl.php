<?php
/* Smarty version 4.2.1, created on 2022-12-18 10:01:09
  from '/var/www/html/control/themes/default/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '4.2.1',
  'unifunc' => 'content_639ed6d595b554_18668960',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '1dd84481327db7313e620e7ad452cd8977e39629' => 
    array (
      0 => '/var/www/html/control/themes/default/template/content.tpl',
      1 => 1666787715,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_639ed6d595b554_18668960 (Smarty_Internal_Template $_smarty_tpl) {
?><div id="ajax_confirmation" class="alert alert-success hide"></div>
<div id="ajaxBox" style="display:none"></div>
<div id="content-message-box"></div>

<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
	<?php echo $_smarty_tpl->tpl_vars['content']->value;?>

<?php }
}
}
