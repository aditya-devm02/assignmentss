<script setup>
import { ref, onMounted } from 'vue';

console.log('App.vue rendering');

const movie = ref(null);
const showTrailer = ref(false);
const mobileNavOpen = ref(false);

onMounted(async () => {
  const res = await fetch('http://www.omdbapi.com/?i=tt3896198&apikey=d2132124');
  movie.value = await res.json();
  pickRandomQuote();
});

function openTrailer() {
  showTrailer.value = true;
}
function closeTrailer() {
  showTrailer.value = false;
}
function toggleMobileNav() {
  mobileNavOpen.value = !mobileNavOpen.value;
}
function closeMobileNav() {
  mobileNavOpen.value = false;
}

const tagline = 'Anyone can save the galaxy once.';
const crew = [
  { name: 'James Gunn', role: 'Director, Writer' },
  { name: 'Bill Mantlo', role: 'Characters' },
  { name: 'Keith Giffen', role: 'Characters' },
  { name: 'Steve Englehart', role: 'Characters' },
  { name: 'Larry Lieber', role: 'Characters' },
  { name: 'Steve Gan', role: 'Characters' },
  { name: 'Jack Kirby', role: 'Characters' },
  { name: 'Val Mayerik', role: 'Characters' },
  { name: 'Jim Starlin', role: 'Characters' },
  { name: 'Stan Lee', role: 'Characters' },
  { name: 'Steve Gerber', role: 'Characters' },
];
const cast = [
  { name: 'Chris Pratt', role: 'Peter Quill / Star-Lord', img: 'https://www.themoviedb.org/t/p/w138_and_h175_face/83o3koL82jt30EJ0rz4Bnzrt2dd.jpg' },
  { name: 'Zoe Saldaña', role: 'Gamora', img: 'https://www.themoviedb.org/t/p/w138_and_h175_face/iOVbUH20il632nj2v01NCtYYeSg.jpg' },
  { name: 'Dave Bautista', role: 'Drax', img: 'https://www.themoviedb.org/t/p/w138_and_h175_face/sg0D2h4l6Fq5pX6f3g1yqLqKpU2.jpg' },
  { name: 'Vin Diesel', role: 'Baby Groot (voice)', img: 'https://www.themoviedb.org/t/p/w138_and_h175_face/3oWEuo0e8Nx8JvkqYCDec2iMY6K.jpg' },
  { name: 'Bradley Cooper', role: 'Rocket (voice)', img: 'https://www.themoviedb.org/t/p/w138_and_h175_face/5XBzD5WuTyVQZeS4VI25z2moMeY.jpg' },
  { name: 'Kurt Russell', role: 'Ego', img: 'https://www.themoviedb.org/t/p/w138_and_h175_face/1YjdSym1jTG7xjHSI0yGGWEsw5i.jpg' },
  { name: 'Michael Rooker', role: 'Yondu', img: 'https://www.themoviedb.org/t/p/w138_and_h175_face/4A5f5bYwFJTZ5p1U5Zl9oQJ6Q0y.jpg' },
];
const socialLinks = [
  { icon: '🌐', label: 'Website' },
  { icon: '🐦', label: 'Twitter' },
  { icon: '📸', label: 'Instagram' },
  { icon: '🔵', label: 'Facebook' },
];
const stats = [
  { label: 'Status', value: 'Released' },
  { label: 'Original Language', value: 'English' },
  { label: 'Budget', value: '$200,000,000' },
  { label: 'Revenue', value: '$863,756,051' },
];

// Unique Feature 1: Random Movie Fact
const facts = [
  'James Gunn, the director, also voices Baby Groot’s dancing moves.',
  'The film’s opening sequence took months to animate due to Baby Groot.',
  'Kurt Russell improvised many of his lines as Ego.',
  'The movie’s soundtrack reached #1 on the Billboard charts.',
  'Stan Lee makes a cameo as an informant to the Watchers.'
];
const randomFact = ref('');
const showFact = ref(false);
function showRandomFact() {
  const idx = Math.floor(Math.random() * facts.length);
  randomFact.value = facts[idx];
  showFact.value = false;
  setTimeout(() => { showFact.value = true; }, 50); // trigger animation
}

// Unique Feature 2: Movie Quote of the Day


const guardians = [
  { name: 'Star-Lord', emoji: '🪐' },
  { name: 'Gamora', emoji: '🗡️' },
  { name: 'Drax', emoji: '💪' },
  { name: 'Rocket', emoji: '🦝' },
  { name: 'Groot', emoji: '🌱' },
];
const pollVotes = ref([0, 0, 0, 0, 0]);
const pollVoted = ref(null);
function voteGuardian(idx) {
  console.log('Vote clicked for guardian:', idx, guardians[idx].name);
  if (pollVoted.value === null) {
    pollVotes.value[idx]++;
    pollVoted.value = idx;
    console.log('Vote registered! New votes:', pollVotes.value);
  } else {
    console.log('Already voted for:', pollVoted.value);
  }
}
</script>

<template>
  <!-- Main Navigation Bar -->
  <nav class="tmdb-navbar">
    <div class="tmdb-navbar-content">
      <div class="tmdb-logo">
        <span class="tmdb-logo-text">TMDB</span>
      </div>
      <div class="tmdb-nav-links">
        <a href="#" class="tmdb-nav-link">Movies</a>
        <a href="#" class="tmdb-nav-link">TV Shows</a>
        <a href="#" class="tmdb-nav-link">People</a>
        <a href="#" class="tmdb-nav-link">More</a>
      </div>
      <div class="tmdb-nav-actions">
        <button class="tmdb-add-btn">+</button>
        <button class="tmdb-lang-btn">EN</button>
        <button class="tmdb-login-btn">Login</button>
        <button class="tmdb-join-btn">Join TMDB</button>
        <button class="tmdb-search-btn">🔍</button>
      </div>
    </div>
  </nav>

  <!-- Secondary Navigation Bar -->
  <nav class="tmdb-secondary-nav">
    <div class="tmdb-secondary-content">
      <a href="#" class="tmdb-secondary-link active">Overview <span class="dropdown">▼</span></a>
      <a href="#" class="tmdb-secondary-link">Media <span class="dropdown">▼</span></a>
      <a href="#" class="tmdb-secondary-link">Fandom <span class="dropdown">▼</span></a>
      <a href="#" class="tmdb-secondary-link">Share <span class="dropdown">▼</span></a>
    </div>
  </nav>

  <div v-if="movie" class="tmdb-main-content">
    <!-- Hero Section -->
    <div class="tmdb-hero">
      <div class="tmdb-hero-content">
        <!-- Left Side - Movie Poster -->
        <div class="tmdb-poster-section">
          <div class="tmdb-poster-container">
            <img :src="movie.Poster" :alt="movie.Title" class="tmdb-poster" />
            <div class="tmdb-streaming-badge">
              <div class="tmdb-streaming-text">Now Streaming</div>
              <div class="tmdb-watch-now">Watch Now</div>
              <div class="tmdb-disney-logo">Disney+</div>
            </div>
          </div>
          <h1 class="tmdb-movie-title">GUARDIANS OF THE GALAXY VOL. 2</h1>
        </div>

        <!-- Right Side - Movie Details -->
        <div class="tmdb-details-section">
          <div class="tmdb-movie-header">
            <h1 class="tmdb-title">{{ movie.Title }} <span class="tmdb-year">({{ movie.Year }})</span></h1>
            <div class="tmdb-meta-info">
              <span class="tmdb-rating">12</span>
              <span class="tmdb-release-date">05/02/2017 (KR)</span>
              <span class="tmdb-genres">Adventure, Action, Science Fiction</span>
              <span class="tmdb-runtime">2h 17m</span>
            </div>
          </div>

          <div class="tmdb-score-section">
            <div class="tmdb-user-score">
              <div class="tmdb-score-circle">
                <span class="tmdb-score-number">76</span>
                <span class="tmdb-score-percent">%</span>
              </div>
              <div class="tmdb-score-label">User Score</div>
            </div>
          </div>

          <div class="tmdb-action-buttons">
            <button class="tmdb-action-btn" aria-label="Add to list">
              <span>📋</span>
            </button>
            <button class="tmdb-action-btn" aria-label="Favorite">
              <span>🫶</span>
            </button>
            <button class="tmdb-action-btn" aria-label="Watchlist">
              <span>🔖</span>
            </button>
            <button class="tmdb-action-btn" aria-label="Rate">
              <span>⭐</span>
            </button>
            <button class="tmdb-play-trailer-btn" @click="openTrailer">
              <span class="play-icon">▶</span>
              <span>Play Trailer</span>
            </button>
          </div>

          <div class="tmdb-tagline">Obviously.</div>

          <!-- Interactive Features Section -->
          <div class="tmdb-features-section">
            <!-- Random Fact Feature -->
            <div class="tmdb-feature-card">
              <button class="tmdb-fact-btn" @click="showRandomFact">Show a Random Fact</button>
              <transition name="fade">
                <div v-if="showFact" class="tmdb-fact-card">{{ randomFact }}</div>
              </transition>
            </div>

            <!-- Fan Poll Feature -->
            <div class="tmdb-feature-card">
              <div class="tmdb-poll-title">Fan Poll: Who's Your Favorite Guardian?</div>
              <div class="tmdb-poll-options">
                <button
                  v-for="(g, idx) in guardians"
                  :key="g.name"
                  :disabled="pollVoted !== null"
                  :class="['tmdb-poll-btn', { selected: pollVoted === idx }]"
                  @click="voteGuardian(idx)"
                >
                  <span class="tmdb-poll-emoji">{{ g.emoji }}</span> {{ g.name }}
                </button>
              </div>
              <div class="tmdb-poll-results">
                <div
                  v-for="(g, idx) in guardians"
                  :key="g.name + '-bar'"
                  class="tmdb-poll-bar-row"
                >
                  <span class="tmdb-poll-emoji">{{ g.emoji }}</span>
                  <div class="tmdb-poll-bar-bg">
                    <div
                      class="tmdb-poll-bar"
                      :class="{ lead: pollVotes[idx] === Math.max(...pollVotes) && pollVotes[idx] > 0 }"
                      :style="{ width: (pollVotes[idx] * 30 + 10) + 'px', transition: 'width 0.5s' }"
                    ></div>
                  </div>
                  <span class="tmdb-poll-count">{{ pollVotes[idx] }}</span>
                </div>
              </div>
              <div v-if="pollVoted !== null" class="tmdb-poll-thankyou">Thank you for voting!</div>
            </div>
          </div>

          <div class="tmdb-overview">
            <h3>Overview</h3>
            <p>The Guardians must fight to keep their newfound family together as they unravel the mysteries of Peter Quill's true parentage.</p>
          </div>

          <div class="tmdb-crew-section">
            <div class="tmdb-crew-grid">
              <div v-for="(person, idx) in crew.slice(0, 10)" :key="idx" class="tmdb-crew-item">
                <div class="tmdb-crew-name">{{ person.name }}</div>
                <div class="tmdb-crew-role">{{ person.role }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Trailer Modal -->
    <div v-if="showTrailer" class="tmdb-modal" tabindex="-1" aria-modal="true" role="dialog">
      <div class="tmdb-modal-backdrop" @click="closeTrailer" aria-label="Close trailer"></div>
      <div class="tmdb-modal-content" role="document">
        <button class="tmdb-modal-close" @click="closeTrailer" aria-label="Close trailer">&times;</button>
        <iframe
          width="560"
          height="315"
          src="https://www.youtube.com/embed/dW1BIid8Osg?autoplay=1"
          title="Guardians of the Galaxy Vol. 2 Trailer"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
        ></iframe>
      </div>
    </div>
  </div>
  <div v-else class="tmdb-loading">
    Loading...
  </div>
</template>

<style scoped>
/* Reset and base styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Source Sans Pro', Arial, sans-serif;
  background-color: #0f1419;
  color: #ffffff;
  line-height: 1.4;
}

/* Main Navigation Bar */
.tmdb-navbar {
  background-color: #032541;
  border-bottom: 1px solid #1f1f1f;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  height: 64px;
}

.tmdb-navbar-content {
  max-width: 1300px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  padding: 0 40px;
}

.tmdb-logo {
  display: flex;
  align-items: center;
}

.tmdb-logo-text {
  font-size: 24px;
  font-weight: 700;
  color: #01b4e4;
  text-decoration: none;
  border-bottom: 2px solid #01b4e4;
  padding-bottom: 2px;
}

.tmdb-nav-links {
  display: flex;
  gap: 32px;
}

.tmdb-nav-link {
  color: #ffffff;
  text-decoration: none;
  font-size: 16px;
  font-weight: 600;
  transition: color 0.2s;
}

.tmdb-nav-link:hover {
  color: #01b4e4;
}

.tmdb-nav-actions {
  display: flex;
  align-items: center;
  gap: 16px;
}

.tmdb-add-btn {
  background: none;
  border: none;
  color: #ffffff;
  font-size: 20px;
  font-weight: 700;
  cursor: pointer;
  padding: 8px;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.tmdb-add-btn:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.tmdb-lang-btn,
.tmdb-login-btn,
.tmdb-join-btn {
  background: none;
  border: none;
  color: #ffffff;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  padding: 8px 16px;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.tmdb-lang-btn:hover,
.tmdb-login-btn:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.tmdb-join-btn {
  background-color: #01b4e4;
  color: #ffffff;
}

.tmdb-join-btn:hover {
  background-color: #0399c6;
}

.tmdb-search-btn {
  background: none;
  border: none;
  color: #ffffff;
  font-size: 18px;
  cursor: pointer;
  padding: 8px;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.tmdb-search-btn:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

/* Secondary Navigation */
.tmdb-secondary-nav {
  background-color: #ffffff;
  border-bottom: 1px solid #e3e3e3;
  position: sticky;
  top: 64px;
  z-index: 999;
}

.tmdb-secondary-content {
  max-width: 1300px;
  margin: 0 auto;
  display: flex;
  gap: 32px;
  padding: 0 40px;
}

.tmdb-secondary-link {
  color: #000000;
  text-decoration: none;
  font-size: 16px;
  font-weight: 600;
  padding: 16px 0;
  border-bottom: 2px solid transparent;
  transition: border-color 0.2s;
  display: flex;
  align-items: center;
  gap: 4px;
}

.tmdb-secondary-link.active {
  color: #01b4e4;
  border-bottom-color: #01b4e4;
}

.tmdb-secondary-link:hover {
  color: #01b4e4;
}

.dropdown {
  font-size: 12px;
  color: #666666;
}

/* Main Content */
.tmdb-main-content {
  margin-top: 64px;
  background-color: #0f1419;
  min-height: calc(100vh - 64px);
}

.tmdb-hero {
  background: linear-gradient(135deg, #0f1419 0%, #1a1d29 100%);
  padding: 40px 0;
}

.tmdb-hero-content {
  max-width: 1300px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 40px;
  padding: 0 40px;
}

/* Poster Section */
.tmdb-poster-section {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.tmdb-poster-container {
  position: relative;
}

.tmdb-poster {
  width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.tmdb-streaming-badge {
  position: absolute;
  bottom: 16px;
  left: 16px;
  right: 16px;
  background: linear-gradient(135deg, #1f80e0 0%, #0d5aa7 100%);
  color: #ffffff;
  padding: 12px 16px;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0 4px 16px rgba(31, 128, 224, 0.3);
}

.tmdb-streaming-text {
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 4px;
}

.tmdb-watch-now {
  font-size: 12px;
  opacity: 0.9;
  margin-bottom: 4px;
}

.tmdb-disney-logo {
  font-size: 10px;
  font-weight: 700;
  opacity: 0.8;
}

.tmdb-movie-title {
  font-size: 20px;
  font-weight: 700;
  color: #ffffff;
  text-align: center;
  line-height: 1.2;
}

/* Details Section */
.tmdb-details-section {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.tmdb-movie-header {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.tmdb-title {
  font-size: 32px;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.2;
}

.tmdb-year {
  font-weight: 400;
  color: #b0b0b0;
}

.tmdb-meta-info {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  align-items: center;
  font-size: 16px;
  color: #b0b0b0;
}

.tmdb-rating {
  background-color: #333333;
  color: #ffffff;
  padding: 4px 8px;
  border-radius: 4px;
  font-weight: 600;
  font-size: 14px;
}

.tmdb-release-date,
.tmdb-genres,
.tmdb-runtime {
  color: #b0b0b0;
}

/* Score Section */
.tmdb-score-section {
  display: flex;
  align-items: center;
  gap: 24px;
}

.tmdb-user-score {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.tmdb-score-circle {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: linear-gradient(135deg, #21d07a 0%, #1a9f5f 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  border: 3px solid #21d07a;
}

.tmdb-score-number {
  font-size: 20px;
  font-weight: 700;
  color: #ffffff;
}

.tmdb-score-percent {
  font-size: 12px;
  font-weight: 600;
  color: #ffffff;
  position: absolute;
  top: 8px;
  right: 8px;
}

.tmdb-score-label {
  font-size: 12px;
  color: #b0b0b0;
  text-align: center;
}

/* Action Buttons */
.tmdb-action-buttons {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}

.tmdb-action-btn {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background-color: #333333;
  border: none;
  color: #ffffff;
  font-size: 18px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.2s;
}

.tmdb-action-btn:hover {
  background-color: #444444;
}

.tmdb-play-trailer-btn {
  background: linear-gradient(135deg, #01b4e4 0%, #0399c6 100%);
  border: none;
  color: #ffffff;
  padding: 12px 24px;
  border-radius: 24px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: background 0.2s;
}

.tmdb-play-trailer-btn:hover {
  background: linear-gradient(135deg, #0399c6 0%, #0284b3 100%);
}

.play-icon {
  font-size: 14px;
}

/* Tagline */
.tmdb-tagline {
  font-size: 18px;
  color: #b0b0b0;
  font-style: italic;
}

/* Interactive Features Section */
.tmdb-features-section {
  display: flex;
  flex-direction: column;
  gap: 24px;
  margin: 24px 0;
}

.tmdb-feature-card {
  background: linear-gradient(135deg, #1a1d29 0%, #0f1419 100%);
  border: 1px solid #333333;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}

/* Random Fact Feature */
.tmdb-fact-btn {
  background: linear-gradient(135deg, #01b4e4 0%, #0399c6 100%);
  border: none;
  color: #ffffff;
  padding: 12px 24px;
  border-radius: 24px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
  width: 100%;
}

.tmdb-fact-btn:hover {
  background: linear-gradient(135deg, #0399c6 0%, #0284b3 100%);
}

.tmdb-fact-card {
  margin-top: 16px;
  padding: 16px;
  background: rgba(1, 180, 228, 0.1);
  border: 1px solid rgba(1, 180, 228, 0.3);
  border-radius: 8px;
  color: #e0e0e0;
  font-size: 16px;
  line-height: 1.6;
  animation: fadeIn 0.3s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Fan Poll Feature */
.tmdb-poll-title {
  font-size: 20px;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 16px;
  text-align: center;
}

.tmdb-poll-options {
  display: flex;
  gap: 12px;
  margin-bottom: 20px;
  flex-wrap: wrap;
  justify-content: center;
}

.tmdb-poll-btn {
  background: linear-gradient(135deg, #01b4e4 0%, #0399c6 100%);
  color: #ffffff;
  border: none;
  border-radius: 20px;
  padding: 8px 16px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 6px;
}

.tmdb-poll-btn:hover {
  background: linear-gradient(135deg, #0399c6 0%, #0284b3 100%);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(1, 180, 228, 0.3);
}

.tmdb-poll-btn:active {
  transform: translateY(0);
}

.tmdb-poll-btn:disabled {
  background: #666666;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.tmdb-poll-btn.selected {
  background: linear-gradient(135deg, #21d07a 0%, #1a9f5f 100%);
  box-shadow: 0 4px 12px rgba(33, 208, 122, 0.3);
}

.tmdb-poll-emoji {
  font-size: 16px;
}

.tmdb-poll-results {
  margin-top: 16px;
}

.tmdb-poll-bar-row {
  display: flex;
  align-items: center;
  margin-bottom: 8px;
  gap: 12px;
}

.tmdb-poll-bar-bg {
  background: #333333;
  border-radius: 8px;
  width: 120px;
  height: 16px;
  overflow: hidden;
  flex-shrink: 0;
}

.tmdb-poll-bar {
  background: linear-gradient(135deg, #21d07a 0%, #1a9f5f 100%);
  height: 100%;
  border-radius: 8px 0 0 8px;
  transition: width 0.5s ease;
}

.tmdb-poll-bar.lead {
  background: linear-gradient(135deg, #01b4e4 0%, #0399c6 100%);
  box-shadow: 0 0 8px rgba(1, 180, 228, 0.5);
}

.tmdb-poll-count {
  font-weight: 700;
  color: #ffffff;
  min-width: 20px;
  text-align: center;
}

.tmdb-poll-thankyou {
  margin-top: 16px;
  color: #21d07a;
  font-weight: 600;
  font-size: 16px;
  text-align: center;
  padding: 12px;
  background: rgba(33, 208, 122, 0.1);
  border: 1px solid rgba(33, 208, 122, 0.3);
  border-radius: 8px;
}

/* Overview */
.tmdb-overview h3 {
  font-size: 20px;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 12px;
}

.tmdb-overview p {
  font-size: 16px;
  color: #e0e0e0;
  line-height: 1.6;
}

/* Crew Section */
.tmdb-crew-section {
  margin-top: 16px;
}

.tmdb-crew-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 16px;
}

.tmdb-crew-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.tmdb-crew-name {
  font-size: 14px;
  font-weight: 600;
  color: #ffffff;
}

.tmdb-crew-role {
  font-size: 12px;
  color: #b0b0b0;
}

/* Modal */
.tmdb-modal {
  position: fixed;
  inset: 0;
  z-index: 2000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.tmdb-modal-backdrop {
  position: absolute;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.8);
}

.tmdb-modal-content {
  position: relative;
  background-color: #0f1419;
  border-radius: 8px;
  padding: 24px;
  max-width: 90vw;
  max-height: 90vh;
  overflow: hidden;
}

.tmdb-modal-close {
  position: absolute;
  top: 16px;
  right: 16px;
  background: none;
  border: none;
  color: #ffffff;
  font-size: 24px;
  cursor: pointer;
  z-index: 2001;
}

/* Loading */
.tmdb-loading {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  font-size: 18px;
  color: #b0b0b0;
}

/* Responsive Design */
@media (max-width: 768px) {
  .tmdb-navbar-content {
    padding: 0 20px;
  }
  
  .tmdb-nav-links {
    display: none;
  }
  
  .tmdb-secondary-content {
    padding: 0 20px;
    gap: 16px;
  }
  
  .tmdb-hero-content {
    grid-template-columns: 1fr;
    gap: 24px;
    padding: 0 20px;
  }
  
  .tmdb-poster-section {
    max-width: 300px;
    margin: 0 auto;
  }
  
  .tmdb-action-buttons {
    justify-content: center;
  }
  
  .tmdb-crew-grid {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  }
}
</style>