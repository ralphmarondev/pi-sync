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
                    // TODO: Uncomment this when onboarding screen is completed!
                    preferences.setFirstLaunch()
                    navController.popBackStack() // we are not going back here
                    navController.navigate(Routes.Auth) {
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
                    navController.popBackStack() // we are not going back here unless on logout
                    navController.navigate(Routes.Home) {
                        launchSingleTop = true
                    }
                }
            )
        }
        composable<Routes.Home> {
            HomeNavigation(
                navigateToAuth = {
                    navController.navigate(Routes.Auth) {
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

        composable<Routes.Developer> { }

        composable<Routes.Licenses> { }
    }
}