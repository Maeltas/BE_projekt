<?php
/* Smarty version 4.2.1, created on 2022-12-18 10:00:02
  from '/var/www/html/modules/ps_emailsubscription/views/templates/admin/list_action_viewcustomer.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '4.2.1',
  'unifunc' => 'content_639ed6929f0177_64869119',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '9f421a091fbdbd571bc405e02d078db476971759' => 
    array (
      0 => '/var/www/html/modules/ps_emailsubscription/views/templates/admin/list_action_viewcustomer.tpl',
      1 => 1625757885,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_639ed6929f0177_64869119 (Smarty_Internal_Template $_smarty_tpl) {
?><a href="<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['href']->value,'html','UTF-8' ));?>
" class="edit btn btn-default <?php if ($_smarty_tpl->tpl_vars['disable']->value) {?>disabled<?php }?>" title="<?php echo $_smarty_tpl->tpl_vars['action']->value;?>
" >
	<i class="icon-search-plus"></i> <?php echo $_smarty_tpl->tpl_vars['action']->value;?>

</a>
<?php }
}
