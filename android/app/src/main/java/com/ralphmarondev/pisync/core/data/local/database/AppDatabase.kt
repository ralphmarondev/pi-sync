package com.ralphmarondev.pisync.core.data.local.database

import androidx.room.Database
import androidx.room.RoomDatabase
import com.ralphmarondev.pisync.core.data.local.database.dao.RoomDao
import com.ralphmarondev.pisync.core.domain.model.Room

@Database(
    entities = [Room::class],
    version = 1,
    exportSchema = false
)
abstract class AppDatabase : RoomDatabase() {
    abstract fun roomDao(): RoomDao

    companion object {
        const val NAME = "pisync_database"
    }
}