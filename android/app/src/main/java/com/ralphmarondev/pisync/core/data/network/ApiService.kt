package com.ralphmarondev.pisync.core.data.network

import com.ralphmarondev.pisync.core.domain.Result
import com.ralphmarondev.pisync.features.auth.domain.model.PasswordHintResponse
import com.ralphmarondev.pisync.features.auth.domain.model.User
import com.ralphmarondev.pisync.features.history.domain.model.DoorLog
import com.ralphmarondev.pisync.features.home.domain.model.DoorActionRequest
import com.ralphmarondev.pisync.features.home.domain.model.DoorActionResponse
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST
import retrofit2.http.Path

interface ApiService {
    @POST("login/")
    suspend fun login(@Body user: User): Result

    @GET("user/password-hint/{username}/")
    suspend fun getPasswordHint(
        @Path("username") username: String
    ): PasswordHintResponse

    @POST("door/open/{id}/")
    suspend fun openDoor(
        @Path("id") doorId: Int,
        @Body request: DoorActionRequest
    ): DoorActionResponse

    @POST("door/close/{id}/")
    suspend fun closeDoor(
        @Path("id") doorId: Int,
        @Body request: DoorActionRequest
    ): DoorActionResponse

    @GET("door/status/{id}/")
    suspend fun doorStatus(
        @Path("id") doorId: Int
    ): DoorActionResponse

    @GET("history/")
    suspend fun getHistory(): List<DoorLog>
}