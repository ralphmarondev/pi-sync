package com.ralphmarondev.pisync.features.overview.data.network

import com.ralphmarondev.pisync.features.overview.data.models.UserDetailResponse
import retrofit2.http.GET
import retrofit2.http.Path

interface UserDetailApiService {

    @GET("user/username/{username}/")
    suspend fun getUserDetailByUsername(
        @Path("username") username: String
    ): UserDetailResponse
}