package com.ralphmarondev.pisync.navigation

import android.annotation.SuppressLint
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.History
import androidx.compose.material.icons.filled.Home
import androidx.compose.material.icons.filled.Settings
import androidx.compose.material.icons.outlined.History
import androidx.compose.material.icons.outlined.Home
import androidx.compose.material.icons.outlined.Settings
import androidx.compose.material3.Icon
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.ralphmarondev.pisync.features.history.presentation.HistoryScreen
import com.ralphmarondev.pisync.features.home.presentation.HomeScreen
import com.ralphmarondev.pisync.features.settings.presentation.overview.SettingScreen

@SuppressLint("UnusedMaterial3ScaffoldPaddingParameter")
@Composable
fun HomeNavigation(
    navigateToAuth: () -> Unit,
    toggleDarkTheme: () -> Unit,
    darkTheme: Boolean,
    appNavigation: NavHostController,
    navController: NavHostController = rememberNavController()
) {
    var selectedScreen by rememberSaveable {
        mutableIntStateOf(0)
    }
    val homeNavItems = listOf(
        HomeNavItems(
            name = "Home",
            defaultIcon = Icons.Outlined.Home,
            selectedIcon = Icons.Filled.Home,
            isSelected = selectedScreen == 0,
            onClick = {
                selectedScreen = 0
                navController.navigate(Routes.HomeNav.Dashboard) {
                    launchSingleTop = true
                }
            }
        ),
        HomeNavItems(
            name = "History",
            defaultIcon = Icons.Outlined.History,
            selectedIcon = Icons.Filled.History,
            isSelected = selectedScreen == 1,
            onClick = {
                selectedScreen = 1
                navController.navigate(Routes.HomeNav.History) {
                    launchSingleTop = true
                }
            }
        ),
        HomeNavItems(
            name = "Settings",
            defaultIcon = Icons.Outlined.Settings,
            selectedIcon = Icons.Filled.Settings,
            isSelected = selectedScreen == 2,
            onClick = {
                selectedScreen = 2
                navController.navigate(Routes.HomeNav.Settings) {
                    launchSingleTop = true
                }
            }
        )
    )

    Scaffold(
        bottomBar = {
            NavigationBar {
                homeNavItems.forEachIndexed { _, item ->
                    NavigationBarItem(
                        selected = item.isSelected,
                        onClick = { item.onClick() },
                        label = {
                            Text(
                                text = item.name
                            )
                        },
                        icon = {
                            Icon(
                                imageVector = if (item.isSelected) item.selectedIcon else item.defaultIcon,
                                contentDescription = item.name
                            )
                        }
                    )
                }
            }
        }
    ) {
        NavHost(
            navController = navController,
            startDestination = Routes.HomeNav.Dashboard
        ) {
            composable<Routes.HomeNav.Dashboard> {
                HomeScreen(
                    darkTheme = darkTheme,
                    toggleDarkTheme = toggleDarkTheme
                )
            }
            composable<Routes.HomeNav.History> {
                HistoryScreen()
            }
            composable<Routes.HomeNav.Settings> {
                SettingScreen(
                    logout = {
                        navController.navigate(Routes.HomeNav.Dashboard) {
                            // clears the back stack ^^ bye:)
                            popUpTo(Routes.HomeNav.Dashboard) {
                                inclusive = true
                            }
                            launchSingleTop = true
                        }
                        selectedScreen = 0
                        navigateToAuth()
                    },
                    darkTheme = darkTheme,
                    toggleDarkTheme = toggleDarkTheme,
                    navigateToAbout = {
                        appNavigation.navigate(Routes.About) {
                            launchSingleTop = true
                        }
                    },
                    navigateToDeveloper = {
                        appNavigation.navigate(Routes.Developer) {
                            launchSingleTop = true
                        }
                    },
                    navigateToLicenses = {
                        appNavigation.navigate(Routes.Licenses) {
                            launchSingleTop = true
                        }
                    }
                )
            }
        }
    }
}

private data class HomeNavItems(
    val name: String,
    val defaultIcon: ImageVector,
    val selectedIcon: ImageVector,
    val isSelected: Boolean,
    val onClick: () -> Unit
)