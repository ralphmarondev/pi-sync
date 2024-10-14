package com.ralphmarondev.pisync.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.ralphmarondev.pisync.features.auth.presentation.AuthScreen
import com.ralphmarondev.pisync.features.home.presentation.HomeScreen

@Composable
fun AppNavigation(
    darkTheme: Boolean,
    toggleDarkTheme: () -> Unit,
    navController: NavHostController = rememberNavController()
) {
    NavHost(
        navController = navController,
        startDestination = Routes.Auth
    ) {
        composable<Routes.Auth> {
            AuthScreen(
                navigateToHome = {
                    navController.navigate(Routes.Home)
                }
            )
        }
        composable<Routes.Home> {
            HomeScreen(
                darkTheme = darkTheme,
                toggleDarkTheme = toggleDarkTheme
            )
        }
    }
}