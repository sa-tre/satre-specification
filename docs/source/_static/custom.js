// Make external links in the navigation menu open in a new tab
document.addEventListener('DOMContentLoaded', function() {
    // Find all links in the navigation sidebar
    const navLinks = document.querySelectorAll('.wy-menu a[href^="http"]');
    
    navLinks.forEach(function(link) {
        // Check if it's an external link (not to the current domain)
        if (!link.href.includes(window.location.hostname)) {
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
        }
    });
    
    // Also handle glossary and architecture links in the table of contents
    const tocLinks = document.querySelectorAll('.toctree-l1 a[href^="http"], .toctree-l2 a[href^="http"]');
    
    tocLinks.forEach(function(link) {
        if (!link.href.includes(window.location.hostname)) {
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
        }
    });
});
