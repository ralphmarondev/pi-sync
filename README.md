# Pi-Sync

Pi-Sync is a thesis project designed to revolutionize access control in condominiums by integrating modern technologies with centralized management. The system features a Raspberry Pi 5 as the core, syncing mobile, web, and desktop platforms for seamless door management and access tracking.

## Features

### Centralized Dashboard

- Built with **Tkinter**, running directly on the Raspberry Pi.
- Manage users and rooms with full CRUD functionality.
- Log all door access activities for monitoring and security.

### Multi-Platform Door Access

- **Mobile App**: Developed with Kotlin and Jetpack Compose Material 3 for Android devices.
- **Web App**: Created using Vue 3 and JavaScript, providing browser-based access.
- **Physical Dashboard**: Raspberry Pi dashboard acts as the primary management system.

### Access Methods

1. **Physical Key**: Traditional key access for backup and simplicity.
2. **Fingerprint Recognition**: Authenticate users with stored biometric data.
3. **Face Recognition**: Captures an image upon successful fingerprint verification for enhanced security.
4. **Mobile Control**: Unlock doors via the mobile app over the network.

### Synchronization

- Real-time syncing of access data and logs across the mobile app, web app, and Raspberry Pi dashboard.

## Activity Logging

- Tracks and records door access events, providing a complete audit trail.

## Repository Structure

```
pi-sync/
├── api/          # Django Rest Framework source code for the backend API
├── android/      # Kotlin-based Android app source code
├── docs/         # Documentation and additional notes
├── raspberrypi/  # Raspberry Pi dashboard source code (Tkinter)
├── web/          # Vue 3 web app source code
```

## Tech Stack

### Hardware

- **Raspberry Pi 5**: The central brain of the system.

### Software

- **Django Rest Framework**: Backend API for managing data and authentication.
- **Kotlin Jetpack Compose**: For building the mobile application.
- **Vue 3 and JavaScript**: For creating the web interface.
- **Tkinter**: For the desktop dashboard application.

### Tools

- **Face Recognition and Fingerprint Modules**: Integrated with the Raspberry Pi for biometric authentication.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.

## About

Pi-Sync is developed as part of our thesis project by Ralph Maron Eda, Jack Cabigayan, Triesha Mae Olunan, and Jezlyn Cabbab. The system aims to enhance security and convenience in condominium access management through the synchronization of mobile, web, and desktop applications.
