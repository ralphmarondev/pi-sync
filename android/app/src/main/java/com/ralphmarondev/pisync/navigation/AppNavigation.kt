package com.ralphmarondev.pisync.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.ralphmarondev.pisync.core.data.preferences.AppPreferences
import com.ralphmarondev.pisync.features.auth.presentation.AuthScreen
import com.ralphmarondev.pisync.features.onboarding.presentation.OnboardingScreen
import com.ralphmarondev.pisync.features.settings.presentation.about.AboutScreen
import com.ralphmarondev.pisync.features.settings.presentation.developer.DeveloperScreen

@Composable
fun AppNavigation(
    darkTheme: Boolean,
    toggleDarkTheme: () -> Unit,
    preferences: AppPreferences,
    navController: NavHostController = rememberNavController()
) {
    val startDestination: Any = when (preferences.isFirstLaunch()) {
        true -> Routes.Onboarding
        false -> Routes.Auth
    }

    NavHost(
        navController = navController,
        startDestination = startDestination
    ) {
        composable<Routes.Onboarding> {
            OnboardingScreen(
                onCompleted = {
                    preferences.setFirstLaunch()
                    navController.navigate(Routes.Auth) {
                        popUpTo<Routes.Onboarding> {
                            inclusive = true
                        }
                        launchSingleTop = true
                    }
                }
            )
        }

        composable<Routes.Auth> {
            AuthScreen(
                darkTheme = darkTheme,
                toggleDarkTheme = toggleDarkTheme,
                navigateToHome = {
                    navController.navigate(Routes.Home) {
                        popUpTo<Routes.Auth> {
                            inclusive = true
                        }
                        launchSingleTop = true
                    }
                }
            )
        }

        composable<Routes.Home> {
            HomeNavigation(
                navigateToAuth = {
                    navController.navigate(Routes.Auth) {
                        popUpTo(navController.graph.startDestinationId) {
                            inclusive = true
                        }
                        launchSingleTop = true
                    }
                },
                darkTheme = darkTheme,
                toggleDarkTheme = toggleDarkTheme,
                appNavigation = navController
            )
        }

        composable<Routes.About> {
            AboutScreen(
                navigateBack = {
                    navController.navigateUp()
                }
            )
        }

        composable<Routes.Developer> {
            DeveloperScreen(
                navigateBack = {
                    navController.navigateUp()
                }
            )
        }

        composable<Routes.Licenses> { }
    }
}