package com.ralphmarondev.pisync.features.overview.data.repositories

import android.util.Log
import com.ralphmarondev.pisync.features.overview.data.mapper.toDomain
import com.ralphmarondev.pisync.features.overview.data.models.DoorActionRequest
import com.ralphmarondev.pisync.features.overview.data.network.DoorApiService
import com.ralphmarondev.pisync.features.overview.domain.model.Door
import com.ralphmarondev.pisync.features.overview.domain.repositories.OverviewRepository

class OverviewRepositoryImpl(
    private val api: DoorApiService
) : OverviewRepository {
    override suspend fun getDoorsByUsername(username: String): List<Door> {
        val response = api.getDoorListByUsername(username)

        return if (response.success) {
            response.doors.toDomain()
        } else {
            emptyList()
        }
    }

    override suspend fun closeDoorById(id: Int, username: String) {
        val response = api.closeDoorById(
            id = id,
            request = DoorActionRequest(
                username = username,
                description = "Closing via mobile app"
            )
        )

        if (response.success) {
            Log.d("App", "Door: $id closed successfully!")
        } else {
            Log.e("App", "Closing door with id: $id failed.")
        }
    }

    override suspend fun openDoorById(id: Int, username: String) {
        val response = api.openDoorById(
            id = id,
            request = DoorActionRequest(
                username = username,
                description = "Opening via mobile app"
            )
        )

        if (response.success) {
            Log.d("App", "Door: $id opened successfully!")
        } else {
            Log.e("App", "Opening door with id: $id failed.")
        }
    }
}