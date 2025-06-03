# Zodiac Sign Finder
#### Video Demo: https://youtu.be/7rO0j0D1ltM
#### Description:
The Zodiac Sign Finder is a full-stack web application designed to bridge astronomy with modern web technology by providing accurate zodiac sign determinations based on precise astronomical date boundaries. Developed as a final project for Harvard's CS50x course, this tool combines backend Python logic with an intuitive frontend interface, offering users both functionality and educational value.

### Astronomical Foundations
Zodiac signs originate from ancient Babylonian astronomy, dividing the ecliptic into twelve 30-degree sectors corresponding to constellations. Modern Western astrology maintains these divisions but accounts for the precession of equinoxes through fixed calendar dates. This application implements the most widely accepted date ranges used by astronomers and astrologers:

- **Aries** (March 21 - April 19): Marks the vernal equinox in the Northern Hemisphere
- **Taurus** (April 20 - May 20): Associated with the Pleiades star cluster
- **Gemini** (May 21 - June 20): Aligns with the Gemini twins Castor and Pollux
- **Cancer** (June 21 - July 22): Contains the Beehive Cluster (M44)
- **Leo** (July 23 - August 22): Features the bright star Regulus
- **Virgo** (August 23 - September 22): Spans the autumnal equinox
- **Libra** (September 23 - October 22): Originally part of Scorpius
- **Scorpio** (October 23 - November 21): Hosts red supergiant Antares
- **Sagittarius** (November 22 - December 21): Points toward galactic center
- **Capricorn** (December 22 - January 19): Ancient "Sea-Goat" constellation
- **Aquarius** (January 20 - February 18): Contains the Helix Nebula
- **Pisces** (February 19 - March 20): Terminal sign of the zodiac wheel

### Technical Architecture
Built using Flask's microservices architecture, the application follows MVC (Model-View-Controller) principles:

**Backend Components**
- **Routing Engine**: Handles HTTP requests through Flask's WSGI interface
- **Date Processor**: Validates inputs using Python's datetime module with leap-year awareness
- **Business Logic**: Implements zodiac calculation through conditional branching
- **Error Handler**: Manages 4xx-class errors (client-side mistakes)

**Frontend Components**
- **Responsive Template**: Adapts to mobile/desktop viewports via CSS media queries
- **User Experience**:
  - Form validation with real-time feedback
  - Preservation of user input during error states
  - Accessible design following WAI-ARIA standards

### Validation System
The application employs a three-tier validation hierarchy:

1. **Structural Validation**
   - Regex pattern matching for ISO 8601 format (YYYY-MM-DD)
   - Rejects malformed strings like "February 30th"

2. **Temporal Validation**
   - Checks date existence (e.g., prevents 2023-02-29)
   - Enforces reasonable year ranges (1900-present)

3. **Astronomical Validation**
   - Handles month-boundary edge cases (e.g., Capricorn spans December-January)
   - Accounts for timezone neutrality using UTC

### Design Philosophy
The project emphasizes:

**Educational Value**
- Demonstrates core CS50 concepts:
  - Memory safety through Python's managed types
  - Abstraction via function modularization
  - Data validation best practices

**Production Readiness**
- Implements Flask's development server warnings
- Includes proper HTTP status codes (200, 400)
- Maintains clean separation of concerns

### Comparative Analysis
Unlike existing zodiac calculators, this solution:

1. Prioritizes **astronomical accuracy** over simplified date ranges
2. Provides **detailed error diagnostics** beyond binary valid/invalid states
3. Maintains **zero dependencies** beyond Flask for easier deployment

### Potential Enhancements
Future iterations could incorporate:
- Natal chart calculations using PyEphem
- Multilingual support through Flask-Babel
- OAuth integration for saving user histories

This project serves as both a practical tool and a demonstration of fundamental programming principles applied to cultural astronomy. By combining rigorous date validation with accessible design, it offers users reliable astrological information while maintaining academic integrity in its implementation.


## Installation & Usage

1. Clone the repository:
   ```bash
   git clone  https://github.com/winnerey/project_app.git
