$(document).ready(function(){

    /* multi-level dropdown */

    $( '.dropdown a.dropdown-toggle' ).on( 'click', function ( e ) {
        /* a */
        var $el = $( this ); 

        /* li */
        var $parent = $( this ).parent(  );

                       /* child ul */
        if ( !$( this ).next().hasClass( 'show' ) ) {
                      /* parent ul: remove .show from descendants */
            $( this ).parents( '.dropdown-menu' ).first().find( '.show' ).removeClass( "show" );
        }

        /* toggle current selection (click) */
                       /* child ul*/
        var $subMenu = $( this ).next( ".dropdown-menu" );  
        $subMenu.toggleClass( 'show' );

        /* next level to the right */
        if ( !$parent.parent().hasClass( 'navbar-nav' ) ) {
            $el.next().css( { "top": $el[0].offsetTop, "left": $parent.outerWidth() - 4 } );
        }

        return false;
    } );


    /* adjusting wagtail native bs 3 bar menu css to fit bs 4 */

    /* add .nav-link to 1st <a> from menu */
    $( 'li.active.dropdown' ).each( function( index, element ){ 
        $(this).children().first().addClass( 'nav-link' )
    });

    /* add .dropdown-item to all <a> except .nav-link */
    $( 'li a' ).each( function( index, element ){ 
        if( !$(this).hasClass( 'nav-link' ) ) {
            $(this).addClass( 'dropdown-item' )
        }
    });


});

