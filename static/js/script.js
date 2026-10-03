/**
 * Raja Narendra Lal Khan Women's College (Autonomous), Medinipur
 * Master Interactive JavaScript Bundle
 */

document.addEventListener('DOMContentLoaded', function () {
  'use strict';

  // =========================================================================
  // 1. MOBILE NAVIGATION & DROPDOWNS
  // =========================================================================
  const mobileToggle = document.getElementById('mobileNavToggle');
  const navMenu = document.getElementById('navbarMenu');

  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', function (e) {
      e.stopPropagation();
      navMenu.classList.toggle('mobile-active');
      const icon = mobileToggle.querySelector('i');
      if (icon) {
        if (navMenu.classList.contains('mobile-active')) {
          icon.classList.remove('fa-bars');
          icon.classList.add('fa-xmark');
        } else {
          icon.classList.remove('fa-xmark');
          icon.classList.add('fa-bars');
        }
      }
    });

    // Close on click outside
    document.addEventListener('click', function (e) {
      if (!navMenu.contains(e.target) && !mobileToggle.contains(e.target)) {
        navMenu.classList.remove('mobile-active');
        const icon = mobileToggle.querySelector('i');
        if (icon) {
          icon.classList.remove('fa-xmark');
          icon.classList.add('fa-bars');
        }
      }
    });
  }

  // Mobile Dropdown toggles
  const dropdownItems = document.querySelectorAll('.nav-item.dropdown');
  dropdownItems.forEach(item => {
    const link = item.querySelector('.nav-link');
    if (link) {
      link.addEventListener('click', function (e) {
        // If on mobile screen (under 768px), prevent default navigation and toggle dropdown
        if (window.innerWidth <= 768) {
          e.preventDefault();
          // Close other open dropdowns
          dropdownItems.forEach(other => {
            if (other !== item) other.classList.remove('dropdown-open');
          });
          item.classList.toggle('dropdown-open');
        }
      });
    }
  });

  // =========================================================================
  // 2. HERO CAROUSEL
  // =========================================================================
  const slides = document.querySelectorAll('.carousel-slide');
  const dots = document.querySelectorAll('.carousel-dot');
  const prevBtn = document.getElementById('heroPrevBtn');
  const nextBtn = document.getElementById('heroNextBtn');
  let currentSlide = 0;
  let carouselInterval = null;

  function showSlide(index) {
    if (!slides.length) return;
    if (index >= slides.length) currentSlide = 0;
    else if (index < 0) currentSlide = slides.length - 1;
    else currentSlide = index;

    slides.forEach((slide, i) => {
      slide.classList.toggle('active', i === currentSlide);
    });

    dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === currentSlide);
    });
  }

  function nextSlide() {
    showSlide(currentSlide + 1);
  }

  function prevSlide() {
    showSlide(currentSlide - 1);
  }

  function startCarouselTimer() {
    if (slides.length > 1) {
      stopCarouselTimer();
      carouselInterval = setInterval(nextSlide, 6500);
    }
  }

  function stopCarouselTimer() {
    if (carouselInterval) {
      clearInterval(carouselInterval);
      carouselInterval = null;
    }
  }

  if (slides.length > 0) {
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        nextSlide();
        startCarouselTimer();
      });
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        prevSlide();
        startCarouselTimer();
      });
    }

    dots.forEach((dot, i) => {
      dot.addEventListener('click', () => {
        showSlide(i);
        startCarouselTimer();
      });
    });

    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
      heroSection.addEventListener('mouseenter', stopCarouselTimer);
      heroSection.addEventListener('mouseleave', startCarouselTimer);
    }

    startCarouselTimer();
  }

  // =========================================================================
  // 3. BACK TO TOP BUTTON
  // =========================================================================
  const backToTopBtn = document.getElementById('backToTopBtn');

  window.addEventListener('scroll', function () {
    if (backToTopBtn) {
      if (window.scrollY > 320) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    }
  });

  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', function () {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // =========================================================================
  // 4. NOTICE BOARD FILTER & LIVE SEARCH (Notices Page)
  // =========================================================================
  const noticeFilterBtns = document.querySelectorAll('.notice-cat-btn');
  const noticeSearchInput = document.getElementById('noticeSearchInput');
  const noticePageItems = document.querySelectorAll('.notice-page-item');
  const noticeNoResults = document.getElementById('noticeNoResults');

  function filterNotices() {
    if (!noticePageItems.length) return;

    let activeCat = 'All';
    noticeFilterBtns.forEach(btn => {
      if (btn.classList.contains('active')) {
        activeCat = btn.getAttribute('data-category') || 'All';
      }
    });

    const query = noticeSearchInput ? noticeSearchInput.value.toLowerCase().trim() : '';
    let matchCount = 0;

    noticePageItems.forEach(item => {
      const itemCat = item.getAttribute('data-category') || '';
      const text = item.textContent.toLowerCase();

      const catMatches = (activeCat === 'All' || itemCat.toLowerCase() === activeCat.toLowerCase());
      const textMatches = (!query || text.includes(query));

      if (catMatches && textMatches) {
        item.style.display = 'flex';
        matchCount++;
      } else {
        item.style.display = 'none';
      }
    });

    if (noticeNoResults) {
      noticeNoResults.style.display = matchCount === 0 ? 'block' : 'none';
    }
  }

  if (noticeFilterBtns.length > 0) {
    noticeFilterBtns.forEach(btn => {
      btn.addEventListener('click', function () {
        noticeFilterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        filterNotices();
      });
    });
  }

  if (noticeSearchInput) {
    noticeSearchInput.addEventListener('input', filterNotices);
  }

  // =========================================================================
  // 5. GALLERY FILTER & LIGHTBOX
  // =========================================================================
  const galleryFilterBtns = document.querySelectorAll('.gallery-filter-btn');
  const galleryCards = document.querySelectorAll('.gallery-item-card');
  const lightboxModal = document.getElementById('lightboxModal');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxCaption = document.getElementById('lightboxCaption');
  const lightboxClose = document.getElementById('lightboxClose');
  const lightboxPrev = document.getElementById('lightboxPrev');
  const lightboxNext = document.getElementById('lightboxNext');

  let currentGalleryIndex = 0;
  let visibleGalleryItems = [];

  function updateVisibleGallery() {
    visibleGalleryItems = Array.from(galleryCards).filter(card => card.style.display !== 'none');
  }

  if (galleryFilterBtns.length > 0) {
    galleryFilterBtns.forEach(btn => {
      btn.addEventListener('click', function () {
        galleryFilterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const cat = btn.getAttribute('data-category') || 'All';
        galleryCards.forEach(card => {
          const cardCat = card.getAttribute('data-category') || '';
          if (cat === 'All' || cardCat.toLowerCase() === cat.toLowerCase()) {
            card.style.display = 'block';
          } else {
            card.style.display = 'none';
          }
        });
        updateVisibleGallery();
      });
    });
  }

  function openLightbox(index) {
    updateVisibleGallery();
    if (!visibleGalleryItems.length) return;
    if (index >= visibleGalleryItems.length) index = 0;
    if (index < 0) index = visibleGalleryItems.length - 1;

    currentGalleryIndex = index;
    const targetItem = visibleGalleryItems[currentGalleryIndex];
    const imgSrc = targetItem.getAttribute('data-image');
    const title = targetItem.getAttribute('data-title');
    const caption = targetItem.getAttribute('data-caption');

    if (lightboxImg) lightboxImg.src = imgSrc;
    if (lightboxCaption) {
      lightboxCaption.innerHTML = `<strong>${title}</strong><br><span style="font-size: 0.85rem; color: #CBD5E1;">${caption}</span>`;
    }
    if (lightboxModal) lightboxModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    if (lightboxModal) lightboxModal.classList.remove('active');
    document.body.style.overflow = '';
  }

  galleryCards.forEach((card, i) => {
    card.addEventListener('click', function () {
      updateVisibleGallery();
      const visibleIndex = visibleGalleryItems.indexOf(card);
      openLightbox(visibleIndex >= 0 ? visibleIndex : 0);
    });
  });

  if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
  if (lightboxPrev) {
    lightboxPrev.addEventListener('click', (e) => {
      e.stopPropagation();
      openLightbox(currentGalleryIndex - 1);
    });
  }
  if (lightboxNext) {
    lightboxNext.addEventListener('click', (e) => {
      e.stopPropagation();
      openLightbox(currentGalleryIndex + 1);
    });
  }

  if (lightboxModal) {
    lightboxModal.addEventListener('click', function (e) {
      if (e.target === lightboxModal) closeLightbox();
    });
  }

  // Keyboard navigation for lightbox
  document.addEventListener('keydown', function (e) {
    if (lightboxModal && lightboxModal.classList.contains('active')) {
      if (e.key === 'Escape') closeLightbox();
      if (e.key === 'ArrowLeft') openLightbox(currentGalleryIndex - 1);
      if (e.key === 'ArrowRight') openLightbox(currentGalleryIndex + 1);
    }
  });

  // =========================================================================
  // 6. FACULTY FILTER (Faculty Page)
  // =========================================================================
  const facultyFilterBtns = document.querySelectorAll('.faculty-filter-btn');
  const facultyCards = document.querySelectorAll('.faculty-card');

  if (facultyFilterBtns.length > 0) {
    facultyFilterBtns.forEach(btn => {
      btn.addEventListener('click', function () {
        facultyFilterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const dept = btn.getAttribute('data-dept') || 'All';
        facultyCards.forEach(card => {
          const cardDept = card.getAttribute('data-dept') || '';
          if (dept === 'All' || cardDept === dept) {
            card.style.display = 'flex';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  // =========================================================================
  // 7. AUTH MODALS (Student & Faculty Login)
  // =========================================================================
  const authModal = document.getElementById('authModal');
  const authTitle = document.getElementById('authTitle');
  const authSubtitle = document.getElementById('authSubtitle');
  const authRoleInput = document.getElementById('authRoleInput');
  const authClose = document.getElementById('authClose');
  const studentLoginBtns = document.querySelectorAll('.student-login-trigger');
  const facultyLoginBtns = document.querySelectorAll('.faculty-login-trigger');

  function openAuthModal(role) {
    if (!authModal) return;
    if (role === 'Faculty') {
      authTitle.textContent = 'Faculty & Staff Portal';
      authSubtitle.textContent = 'Sign in to access faculty attendance, marks entry, and LMS';
      if (authRoleInput) authRoleInput.value = 'faculty';
    } else {
      authTitle.textContent = 'Student ERP Portal';
      authSubtitle.textContent = 'Sign in to access registration, semester results, and fee payments';
      if (authRoleInput) authRoleInput.value = 'student';
    }
    authModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeAuthModal() {
    if (authModal) authModal.classList.remove('active');
    document.body.style.overflow = '';
  }

  studentLoginBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openAuthModal('Student');
    });
  });

  facultyLoginBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openAuthModal('Faculty');
    });
  });

  if (authClose) authClose.addEventListener('click', closeAuthModal);
  if (authModal) {
    authModal.addEventListener('click', function (e) {
      if (e.target === authModal) closeAuthModal();
    });
  }

  // Mock Login Handler
  const authLoginForm = document.getElementById('authLoginForm');
  if (authLoginForm) {
    authLoginForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const user = document.getElementById('authUsername').value.trim();
      const role = authRoleInput ? authRoleInput.value : 'user';
      alert(`Welcome, ${user}! Directing to the ${role.toUpperCase()} ERP dashboard...`);
      closeAuthModal();
    });
  }

  // =========================================================================
  // 8. INTERACTIVE FORM VALIDATION & SMOOTH FOCUS
  // =========================================================================
  const forms = document.querySelectorAll('form.needs-validation');
  forms.forEach(form => {
    form.addEventListener('submit', function (e) {
      const phoneInput = form.querySelector('input[type="tel"]');
      if (phoneInput) {
        const val = phoneInput.value.replace(/[^0-9]/g, '');
        if (val.length < 10) {
          e.preventDefault();
          alert('Please enter a valid 10-digit mobile number.');
          phoneInput.focus();
        }
      }
    });
  });

  console.log("Raja Narendra Lal Khan Women's College Web Portal Initialized Successfully.");
});
