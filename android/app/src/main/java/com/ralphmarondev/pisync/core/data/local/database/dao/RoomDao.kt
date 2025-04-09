package com.ralphmarondev.pisync.core.data.local.database.dao

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import com.ralphmarondev.pisync.core.domain.model.Room

@Dao
interface RoomDao {
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertRoom(room: Room)

    @Query("SELECT * FROM rooms")
    suspend fun getAllRooms(): List<Room>

    @Query("DELETE FROM rooms")
    suspend fun deleteAllRooms()
}