# 10.8 Backup & Restore

## Overview
**Backup & Restore** is the ultimate safety net for the school's digital existence. Hard drives crash, servers get infected with ransomware, and humans delete critical files by mistake. This module ensures that no matter what catastrophe strikes, the school's financial data can be resurrected from a safe checkpoint.

### Real-World Analogy
Think of this as a **Time Machine / Life Insurance**.
- **Backup (Save Game)**: Taking a snapshot of the entire system (Database + Files) at 2:00 AM every night.
- **Restore (Load Game)**: Something goes wrong at 10:00 AM? You simply "rewind time" to the 2:00 AM state.
- **Offsite Storage**: Keeping a copy of the key at a neighbor's house (Cloud Storage) in case your house burns down.

## Purpose
- **Disaster Recovery**: Recover from total server failure or physical theft of the computer.
- **Data Corruption Protection**: Undo the damage caused by a buggy software update or a virus.
- **Audit Compliance**: Regulatory bodies often require schools to maintain 7 years of financial history. Backups ensure this history is preserved even if hardware changes.
- **Testing**: Using a backup of the "Live Data" to create a "Test Server" for trying out new features without risking real data.

## Key Features
- **Automated Scheduler**: "Run Full Backup every night at 12:00 AM." No human intervention needed.
- **Cloud Sync**: Auto-upload the backup zip file to Google Drive, AWS S3, or Dropbox.
- **Point-in-Time Recovery**: "Restore system to how it was onTuesday at 4 PM" (if Transaction Logs are enabled).
- **Encryption**: Backup files are password-protected (AES-256) so that if stolen, the data remains unreadable.

## Real-World Scenarios

### Scenario 1: The Ransomware Nightmare
**Situation**: The Accountant opens a phishing email. A virus locks all files on the PC and demands bitcoin.
**Action**:
1.  Admin wipes the infected computer hard drive.
2.  Reinstalls the OS and Fee Software.
3.  **Restore**: Connects to Google Drive, downloads yesterday's backup, and clicks "Restore".
4.  **Outcome**: Business as usual within 1 hour. Zero money paid to hackers.

### Scenario 2: The "Oops" Moment
**Situation**: Admin accidentally runs "Delete All Class 10 Students" instead of "Class 12". 200 profiles gone.
**Action**:
1.  Admin restores the backup from **1 hour ago**.
2.  **Outcome**: The deleted students reappear. Any data entered in the last 60 minutes is re-entered manually, but the bulk of data is saved.

### Scenario 3: The Audit Request
**Situation**: It is 2026. Tax officer wants to see detailed Fee Receipts of 2021. The current system only holds active data.
**Action**:
1.  Admin locates `Backup_2021_Final.zip` from the archive.
2.  Restores it to a **Local Laptop** (offline).
3.  **Outcome**: Admin generates the required reports from the isolated 2021 environment.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Corrupt Backup** | The backup file is incomplete or damaged. | **Checksum Verification**: The system verifies the integrity (MD5 Hash) of the backup immediately after creating it. If verification fails, it retries and alerts the Admin. |
| **Disk Full** | Server runs out of space while creating a backup. | **Safety Valve**: The system checks for "Free Space > 2x Backup Size" before starting. If insufficient, it halts and sends an SMS Alert: "Backup Failed: Low Disk Space". |
| **Version Mismatch** | Trying to restore a v1.0 backup on v2.0 software. | **Auto-Migration**: The restore tool detects the version difference and automatically runs "Database Migration Scripts" to upgrade the old data structure to the new format. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Backup ID** | String | `BKP-20231012-0200`. |
| **Type** | Enum | Full, Differential, Incremental. |
| **Size** | Size | 500 MB. |
| **Status** | Enum | Success, Failed, Uploaded. |
| **Location** | Path | `D:/Backups/` + `s3://school-bucket/`. |
| **Encryption** | Boolean | True (Password: *****). |

## User Actions
1.  **Backup Now**: Force a manual backup before doing something risky (like Rollover).
2.  **Restore**: The "Red Button" to bring back data. Requires Super Admin password.
3.  **Download**: Save a copy of the backup to a Pen Drive.
4.  **Configure Cloud**: Connect Google Drive API for offsite storage.

## Best Practices
- **3-2-1 Rule**: Keep **3** copies of data, on **2** different media (Disk + Cloud), with **1** copy offsite.
- **Regular Drills**: Once a quarter, actually try to restore a backup to a test server to ensure the files are valid and you know the process.
- **Exclude Media**: Don't backup "Student Photos" every night. They don't change often and take up space. Backup only the Database nightly, and Photos weekly.
