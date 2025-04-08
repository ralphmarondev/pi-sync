package com.ralphmarondev.pisync.features.overview.data.network

import com.ralphmarondev.pisync.features.overview.data.models.DoorActionRequest
import com.ralphmarondev.pisync.features.overview.data.models.DoorActionResponse
import com.ralphmarondev.pisync.features.overview.data.models.DoorListResponse
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST
import retrofit2.http.Path

interface DoorApiService {

    @GET("doors/username/{username}/")
    suspend fun getDoorListByUsername(
        @Path("username") username: String
    ): DoorListResponse

    @POST("door/open/{id}/")
    suspend fun openDoorById(
        @Path("id") id: Int,
        @Body request: DoorActionRequest
    ): DoorActionResponse


    @POST("door/close/{id}/")
    suspend fun closeDoorById(
        @Path("id") id: Int,
        @Body request: DoorActionRequest
    ): DoorActionResponse
}