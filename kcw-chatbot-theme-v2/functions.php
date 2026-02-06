<?php
function kcw_enqueue_assets() {
    wp_enqueue_style('kcw-style', get_stylesheet_uri());
}
add_action('wp_enqueue_scripts', 'kcw_enqueue_assets');
?>