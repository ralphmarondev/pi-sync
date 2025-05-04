namespace PiSync.Home
{
    partial class HomeForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            panel1 = new Panel();
            btnHistory = new Button();
            btnLogout = new Button();
            btnTenants = new Button();
            btnRooms = new Button();
            btnDashboard = new Button();
            panelLabel = new Panel();
            logoLabel = new Label();
            mainPanel = new Panel();
            panel1.SuspendLayout();
            panelLabel.SuspendLayout();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.BackColor = Color.GhostWhite;
            panel1.Controls.Add(btnHistory);
            panel1.Controls.Add(btnLogout);
            panel1.Controls.Add(btnTenants);
            panel1.Controls.Add(btnRooms);
            panel1.Controls.Add(btnDashboard);
            panel1.Controls.Add(panelLabel);
            panel1.Dock = DockStyle.Left;
            panel1.Location = new Point(0, 0);
            panel1.Name = "panel1";
            panel1.Size = new Size(241, 690);
            panel1.TabIndex = 1;
            // 
            // btnHistory
            // 
            btnHistory.BackColor = Color.Lavender;
            btnHistory.Cursor = Cursors.Hand;
            btnHistory.FlatAppearance.BorderSize = 0;
            btnHistory.FlatStyle = FlatStyle.Flat;
            btnHistory.Font = new Font("Courier New", 14F);
            btnHistory.Location = new Point(12, 312);
            btnHistory.Margin = new Padding(0);
            btnHistory.Name = "btnHistory";
            btnHistory.Size = new Size(212, 61);
            btnHistory.TabIndex = 5;
            btnHistory.Text = "HISTORY";
            btnHistory.UseVisualStyleBackColor = true;
            btnHistory.Click += btnHistory_Click;
            // 
            // btnLogout
            // 
            btnLogout.Anchor = AnchorStyles.Bottom | AnchorStyles.Left;
            btnLogout.BackColor = Color.Lavender;
            btnLogout.Cursor = Cursors.Hand;
            btnLogout.FlatAppearance.BorderSize = 0;
            btnLogout.FlatStyle = FlatStyle.Flat;
            btnLogout.Font = new Font("Courier New", 14F);
            btnLogout.Location = new Point(12, 612);
            btnLogout.Margin = new Padding(0);
            btnLogout.Name = "btnLogout";
            btnLogout.Size = new Size(212, 61);
            btnLogout.TabIndex = 4;
            btnLogout.Text = "LOGOUT";
            btnLogout.UseVisualStyleBackColor = true;
            btnLogout.Click += btnLogout_Click;
            // 
            // btnTenants
            // 
            btnTenants.BackColor = Color.Lavender;
            btnTenants.Cursor = Cursors.Hand;
            btnTenants.FlatAppearance.BorderSize = 0;
            btnTenants.FlatStyle = FlatStyle.Flat;
            btnTenants.Font = new Font("Courier New", 14F);
            btnTenants.Location = new Point(12, 239);
            btnTenants.Margin = new Padding(0);
            btnTenants.Name = "btnTenants";
            btnTenants.Size = new Size(212, 61);
            btnTenants.TabIndex = 3;
            btnTenants.Text = "TENANTS";
            btnTenants.UseVisualStyleBackColor = true;
            btnTenants.Click += btnTenants_Click;
            // 
            // btnRooms
            // 
            btnRooms.BackColor = Color.Lavender;
            btnRooms.Cursor = Cursors.Hand;
            btnRooms.FlatAppearance.BorderSize = 0;
            btnRooms.FlatStyle = FlatStyle.Flat;
            btnRooms.Font = new Font("Courier New", 14F);
            btnRooms.Location = new Point(12, 167);
            btnRooms.Margin = new Padding(0);
            btnRooms.Name = "btnRooms";
            btnRooms.Size = new Size(212, 61);
            btnRooms.TabIndex = 2;
            btnRooms.Text = "ROOMS";
            btnRooms.UseVisualStyleBackColor = true;
            btnRooms.Click += btnRooms_Click;
            // 
            // btnDashboard
            // 
            btnDashboard.BackColor = Color.Lavender;
            btnDashboard.Cursor = Cursors.Hand;
            btnDashboard.FlatAppearance.BorderSize = 0;
            btnDashboard.FlatStyle = FlatStyle.Flat;
            btnDashboard.Font = new Font("Courier New", 14F);
            btnDashboard.Location = new Point(12, 96);
            btnDashboard.Margin = new Padding(0);
            btnDashboard.Name = "btnDashboard";
            btnDashboard.Size = new Size(212, 61);
            btnDashboard.TabIndex = 1;
            btnDashboard.Text = "DASHBOARD";
            btnDashboard.UseVisualStyleBackColor = true;
            btnDashboard.Click += btnDashboard_Click;
            // 
            // panelLabel
            // 
            panelLabel.BackColor = Color.MediumPurple;
            panelLabel.Controls.Add(logoLabel);
            panelLabel.Dock = DockStyle.Top;
            panelLabel.Location = new Point(0, 0);
            panelLabel.Name = "panelLabel";
            panelLabel.Size = new Size(241, 79);
            panelLabel.TabIndex = 0;
            panelLabel.MouseDown += panelLabel_MouseDown;
            panelLabel.MouseMove += panelLabel_MouseMove;
            panelLabel.MouseUp += panelLabel_MouseUp;
            // 
            // logoLabel
            // 
            logoLabel.AutoSize = true;
            logoLabel.Font = new Font("Courier New", 16F);
            logoLabel.ForeColor = Color.Lavender;
            logoLabel.Location = new Point(59, 24);
            logoLabel.Name = "logoLabel";
            logoLabel.Size = new Size(109, 30);
            logoLabel.TabIndex = 1;
            logoLabel.Text = "PISYNC";
            logoLabel.MouseDown += logoLabel_MouseDown;
            logoLabel.MouseMove += logoLabel_MouseMove;
            logoLabel.MouseUp += logoLabel_MouseUp;
            // 
            // mainPanel
            // 
            mainPanel.BackColor = SystemColors.HighlightText;
            mainPanel.Dock = DockStyle.Fill;
            mainPanel.Location = new Point(241, 0);
            mainPanel.Name = "mainPanel";
            mainPanel.Size = new Size(884, 690);
            mainPanel.TabIndex = 2;
            // 
            // HomeForm
            // 
            AutoScaleDimensions = new SizeF(14F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1125, 690);
            Controls.Add(mainPanel);
            Controls.Add(panel1);
            Font = new Font("Courier New", 13.8F, FontStyle.Regular, GraphicsUnit.Point, 0);
            FormBorderStyle = FormBorderStyle.None;
            Margin = new Padding(5, 4, 5, 4);
            Name = "HomeForm";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "HomeForm";
            panel1.ResumeLayout(false);
            panelLabel.ResumeLayout(false);
            panelLabel.PerformLayout();
            ResumeLayout(false);
        }

        #endregion
        private Panel panel1;
        private Panel panelLabel;
        private Button btnDashboard;
        private Label logoLabel;
        private Button btnTenants;
        private Button btnRooms;
        private Panel mainPanel;
        private Button btnLogout;
        private Button btnHistory;
    }
}