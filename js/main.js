/*
 * Vicor Distributor Website - Main JavaScript
 * Handles enhanced interactions and dynamic functionality
 */

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initMobileMenu();
    initDropdowns();
    initSmoothScrolling();
    initContactForm();
    initSearchFunctionality();
    initHeaderScrollBehavior();
    initScrollAnimations();

    // Set up performance monitoring
    initPerformanceMonitoring();

    // Add skip link for accessibility
    initSkipLink();
});

// Add skip link for accessibility
function initSkipLink() {
    const skipLink = document.createElement('a');
    skipLink.href = '#main-content';
    skipLink.textContent = 'Skip to main content';
    skipLink.className = 'skip-link';
    document.body.insertBefore(skipLink, document.body.firstChild);
}

// Mobile menu functionality
function initMobileMenu() {
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (!mobileMenuToggle || !navMenu) return;
    
    mobileMenuToggle.addEventListener('click', function() {
        const isExpanded = this.getAttribute('aria-expanded') === 'true';
        this.setAttribute('aria-expanded', !isExpanded);
        
        // Toggle the nav menu visibility
        navMenu.classList.toggle('active');
        
        // Add/remove class to body to prevent scrolling when menu is open
        document.body.classList.toggle('menu-open', !isExpanded);
        
        // Change the hamburger icon to an X when open
        const hamburgerBars = this.querySelectorAll('.hamburger');
        hamburgerBars.forEach(bar => {
            bar.classList.toggle('close');
        });
    });
    
    // Close menu when clicking on a link (for better UX on mobile)
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (window.innerWidth < 768) {
                mobileMenuToggle.click(); // Simulate click to close menu
            }
        });
    });
}

// Dropdown functionality for navigation
function initDropdowns() {
    // On mobile, expand dropdowns when clicked
    if (window.innerWidth < 768) {
        const dropdowns = document.querySelectorAll('.dropdown');
        
        dropdowns.forEach(dropdown => {
            const dropdownLink = dropdown.querySelector('.nav-link');
            
            dropdownLink.addEventListener('click', function(e) {
                // Only prevent default if it's a parent item with dropdown
                if (this.nextElementSibling) {
                    e.preventDefault();
                    const dropdownMenu = this.nextElementSibling;
                    dropdownMenu.classList.toggle('active');
                }
            });
        });
    }
    
    // For larger screens, use hover effect (handled in CSS)
    // This ensures accessibility for keyboard-only users too
}

// Smooth scrolling for anchor links
function initSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // Only handle valid anchor links
            if (href === '#' || href === '#0') {
                e.preventDefault();
                return;
            }
            
            const targetElement = document.querySelector(href);
            
            if (targetElement) {
                e.preventDefault();
                
                // Get target element position
                const offsetTop = targetElement.offsetTop - 80; // Account for fixed header
                
                // Scroll to target with smooth behavior
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
                
                // Update URL without causing scroll
                history.pushState(null, null, href);
            }
        });
    });
}

// Contact form functionality
function initContactForm() {
    const contactForms = document.querySelectorAll('form.contact-form');
    
    contactForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(this);
            
            // Basic validation
            let isValid = true;
            const requiredFields = this.querySelectorAll('[required]');
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error');
                } else {
                    field.classList.remove('error');
                }
            });
            
            // Email validation
            const emailField = this.querySelector('input[type="email"]');
            if (emailField && emailField.value) {
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(emailField.value)) {
                    isValid = false;
                    emailField.classList.add('error');
                } else {
                    emailField.classList.remove('error');
                }
            }
            
            if (!isValid) {
                // Show validation error
                const errorDiv = document.createElement('div');
                errorDiv.className = 'form-error';
                errorDiv.textContent = 'Please fill in all required fields correctly.';
                errorDiv.setAttribute('role', 'alert');
                
                // Remove any existing error messages
                const existingError = this.querySelector('.form-error');
                if (existingError) {
                    existingError.remove();
                }
                
                this.insertBefore(errorDiv, this.firstChild);
                return;
            }
            
            // Show loading state
            const submitButton = this.querySelector('button[type="submit"]') || 
                                this.querySelector('input[type="submit"]');
            const originalText = submitButton.value || submitButton.textContent;
            submitButton.disabled = true;
            submitButton.textContent = 'Sending...';
            
            // In a real implementation, you would send the form data to a server
            // For this example, we'll simulate the submission
            setTimeout(() => {
                // Reset form
                this.reset();
                
                // Show success message
                const successDiv = document.createElement('div');
                successDiv.className = 'form-success';
                successDiv.textContent = 'Thank you for your inquiry! We will contact you shortly.';
                successDiv.setAttribute('role', 'alert');
                
                // Remove any existing messages
                const existingMessage = this.querySelector('.form-error, .form-success');
                if (existingMessage) {
                    existingMessage.remove();
                }
                
                this.insertBefore(successDiv, this.firstChild);
                
                // Reset button
                submitButton.disabled = false;
                submitButton.textContent = originalText;
            }, 1500);
        });
    });
}

// Search functionality
function initSearchFunctionality() {
    const searchInputs = document.querySelectorAll('input[type="search"], .search-input');
    
    searchInputs.forEach(input => {
        // Debounce search to avoid excessive API calls
        let timeout;
        input.addEventListener('input', function() {
            clearTimeout(timeout);
            timeout = setTimeout(() => {
                const query = this.value.trim();
                
                if (query.length > 2) {
                    performSearch(query);
                } else if (query.length === 0) {
                    // Clear results when search is empty
                    clearSearchResults();
                }
            }, 300); // Debounce for 300ms
        });
    });
}

// Perform search (stub implementation)
function performSearch(query) {
    console.log(`Searching for: ${query}`);
    // In a real implementation, this would call an API or search index
    // For now, just log the search query
}

// Clear search results
function clearSearchResults() {
    console.log('Clearing search results');
    // In a real implementation, this would clear search results UI
}

// Performance monitoring
function initPerformanceMonitoring() {
    // Monitor Core Web Vitals
    if ('measure' in performance) {
        // Measure FCP (First Contentful Paint)
        new PerformanceObserver((list) => {
            for (const entry of list.getEntries()) {
                if (entry.name === 'first-contentful-paint') {
                    console.log('FCP:', entry.startTime);
                    // In a real implementation, you would send this to analytics
                }
            }
        }).observe({entryTypes: ['paint']});
        
        // Measure LCP (Largest Contentful Paint)
        new PerformanceObserver((list) => {
            for (const entry of list.getEntries()) {
                console.log('LCP:', entry.startTime);
                // In a real implementation, you would send this to analytics
            }
        }).observe({entryTypes: ['largest-contentful-paint']});
    }
    
    // Track user interactions
    document.addEventListener('click', function(e) {
        // Track important user interactions
        if (e.target.closest('.cta-button') || e.target.closest('a[href*="contact"]')) {
            console.log('CTA clicked:', e.target.textContent || e.target.href);
        }
    });
}

// Utility functions

// Check if element is in viewport (for animations)
function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Debounce function to limit function calls
function debounce(func, wait, immediate) {
    let timeout;
    return function() {
        const context = this;
        const args = arguments;
        const later = function() {
            timeout = null;
            if (!immediate) func.apply(context, args);
        };
        const callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(context, args);
    };
}

// Throttle function to limit function calls
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Header scroll behavior
function initHeaderScrollBehavior() {
    const header = document.querySelector('.header');
    let lastScrollTop = 0;

    if (!header) return;

    window.addEventListener('scroll', throttle(function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        if (scrollTop > 100) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        lastScrollTop = scrollTop;
    }, 10));
}

// Scroll animations for elements
function initScrollAnimations() {
    // Intersection Observer for animations when elements come into view
    if ('IntersectionObserver' in window) {
        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.1
        };

        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        // Observe cards and other elements
        document.querySelectorAll('.card, .section').forEach(el => {
            observer.observe(el);
        });
    }
}

// Get URL parameters
function getUrlParameter(name) {
    name = name.replace(/[[]/, '\\[').replace(/[\]]/, '\\]');
    const regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
    const results = regex.exec(location.search);
    return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
}

// Add class to body based on device type
if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    document.body.classList.add('mobile-device');
} else {
    document.body.classList.add('desktop-device');
}