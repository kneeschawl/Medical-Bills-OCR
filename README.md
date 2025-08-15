# Neural Network & Insurance Claim Module

**Version:** 0.1.0  
**Author:** Your Name  
**Project Type:** FastAPI + Tesseract OCR  

---

## Overview

This module allows users to submit medical bills as images, automatically extract key information (like patient name, date, amount, hospital, diagnosis), and simulate insurance claim validation. The system uses **OCR (Tesseract)** for text recognition and is designed to be integrated into larger e-governance or insurance platforms.  

> ⚠️ Note: This module currently uses **Tesseract OCR**, not a neural network. Neural network-based recognition can be added in future versions.

---

## Features

- Upload medical bills as images (PNG, JPG).  
- Extract relevant fields:  
  - Patient Name  
  - Bill Date  
  - Amount  
  - Hospital  
  - Diagnosis  
- Check for duplicate/fraudulent claims.  
- Submit claims to a simulated insurance system.  
- Track claim status (`approved`/`rejected`).  
- FastAPI REST API with Swagger UI for testing.

---

## Requirements

- Python 3.11+  
- Tesseract OCR installed on your system  
- Python packages:

