<?php
/* Smarty version 4.2.1, created on 2022-12-18 09:55:07
  from 'module:psimagesliderviewstemplat' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '4.2.1',
  'unifunc' => 'content_639ed56bda2607_78405911',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '6c2108a17c7103b6e203f4f0621d4645b56b0114' => 
    array (
      0 => 'module:psimagesliderviewstemplat',
      1 => 1666708672,
      2 => 'module',
    ),
  ),
  'cache_lifetime' => 31536000,
),true)) {
function content_639ed56bda2607_78405911 (Smarty_Internal_Template $_smarty_tpl) {
?>
  <div id="carousel" data-ride="carousel" class="carousel slide" data-interval="5000" data-wrap="true" data-pause="hover" data-touch="true">
    <ol class="carousel-indicators">
            <li data-target="#carousel" data-slide-to="0" class="active"></li>
            <li data-target="#carousel" data-slide-to="1"></li>
          </ol>
    <ul class="carousel-inner" role="listbox" aria-label="Pokaz slajdów">
              <li class="carousel-item active" role="option" aria-hidden="false">
          <a href="https://some_prestashop/brand/4-nvidia">            <figure>
              <img src="https://some_prestashop/modules/ps_imageslider/images/28b98f3cad43e77d895c1b245bf7108ef080f457_nvidia-partner-network-home-page-banner-767-m.jpg" alt="Karty graficzne" loading="lazy" width="1110" height="340">
                              <figcaption class="caption">
                  <h2 class="display-1 text-uppercase">Nvidia</h2>
                  <div class="caption-description"><h3>Karty graficzne nvidia</h3></div>
                </figcaption>
                          </figure>
          </a>        </li>
              <li class="carousel-item " role="option" aria-hidden="true">
          <a href="https://some_prestashop/brand/1-amd">            <figure>
              <img src="https://some_prestashop/modules/ps_imageslider/images/8873c5ba3c2f20b947f7ec800320cbefeef37696_DeDsacZXcAIgeEc.jpg" alt="Procesory" loading="lazy" width="1110" height="340">
                              <figcaption class="caption">
                  <h2 class="display-1 text-uppercase">AMD</h2>
                  <div class="caption-description"><h3>Procesory AMD</h3>
<p>Najlepsze procesory od AMD</p></div>
                </figcaption>
                          </figure>
          </a>        </li>
          </ul>
    <div class="direction" aria-label="Przyciski karuzeli">
      <a class="left carousel-control" href="#carousel" role="button" data-slide="prev" aria-label="Poprzedni">
        <span class="icon-prev hidden-xs" aria-hidden="true">
          <i class="material-icons">&#xE5CB;</i>
        </span>
      </a>
      <a class="right carousel-control" href="#carousel" role="button" data-slide="next" aria-label="Następny">
        <span class="icon-next" aria-hidden="true">
          <i class="material-icons">&#xE5CC;</i>
        </span>
      </a>
    </div>
  </div>
<?php }
}
